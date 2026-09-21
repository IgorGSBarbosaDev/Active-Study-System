"""Read-only integrity checks for the Active Study System Vault."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import re
import sys
from dataclasses import dataclass
from pathlib import Path


VALID_STATUSES = {"Não iniciado", "Estudando", "Praticando", "Consolidado"}
DATE_FIELDS = {"Data criação", "Data último estudo", "Data última revisão", "Data próxima revisão"}
USER_START = "<!-- USER-NOTES:START -->"
USER_END = "<!-- USER-NOTES:END -->"


@dataclass(frozen=True)
class Finding:
    severity: str
    path: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--date", help="Current date in YYYY-MM-DD; defaults to local date.")
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^\s*([^:]+):\s*(.*?)\s*$", line)
        if match:
            fields[match.group(1)] = match.group(2)
    return fields


def check_topic_pairs(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    topics_root = root / "01_TOPICS"
    if not topics_root.exists():
        return [Finding("ERROR", "01_TOPICS", "pasta de tópicos ausente")]
    for folder in sorted((path for path in topics_root.iterdir() if path.is_dir()), key=lambda p: p.name.casefold()):
        main = folder / f"{folder.name}.md"
        questions = folder / f"Perguntas sobre {folder.name}.md"
        for required, label in ((main, "arquivo principal"), (questions, "arquivo de perguntas")):
            if not required.exists():
                findings.append(Finding("ERROR", relative(root, folder), f"{label} ausente: {required.name}"))
        if main.exists():
            findings.extend(check_topic_fields(root, main))
    return findings


def check_topic_fields(root: Path, path: Path) -> list[Finding]:
    findings: list[Finding] = []
    fields = parse_fields(read_text(path))
    status = fields.get("Status", "")
    if status not in VALID_STATUSES:
        findings.append(Finding("ERROR", relative(root, path), f"Status inválido ou vazio: {status or '<vazio>'}"))
    level = fields.get("Nível", "")
    if not level.isdigit() or int(level) not in range(6):
        findings.append(Finding("ERROR", relative(root, path), f"Nível inválido ou vazio: {level or '<vazio>'}"))
    for field in DATE_FIELDS:
        value = fields.get(field, "")
        if not value:
            continue
        try:
            dt.date.fromisoformat(value)
        except ValueError:
            findings.append(Finding("ERROR", relative(root, path), f"{field} inválida: {value}"))
    return findings


def check_user_notes(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for base in (root / "01_TOPICS", root / "05_EXERCISES"):
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            text = read_text(path)
            relevant = "## Minhas anotações" in text or USER_START in text or USER_END in text
            if not relevant:
                continue
            if text.count(USER_START) != 1 or text.count(USER_END) != 1:
                findings.append(Finding("ERROR", relative(root, path), "marcadores USER-NOTES ausentes ou duplicados"))
            elif text.index(USER_START) > text.index(USER_END):
                findings.append(Finding("ERROR", relative(root, path), "marcadores USER-NOTES fora de ordem"))
    return findings


def check_wiki_links(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    pattern = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in pattern.findall(read_text(path)):
            target = target.strip()
            if "/" not in target and "\\" not in target:
                continue
            candidate = root / target.replace("\\", "/")
            if candidate.suffix.casefold() != ".md":
                candidate = candidate.with_suffix(".md")
            if not candidate.exists():
                findings.append(Finding("WARNING", relative(root, path), f"link canônico quebrado: [[{target}]]"))
    return findings


def section_body(text: str, heading: str) -> str | None:
    match = re.search(
        rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else None


def check_exercise_state(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    exercises = root / "05_EXERCISES"
    if not exercises.exists():
        return findings
    for path in exercises.rglob("*.md"):
        if path.name.casefold() == "readme.md":
            continue
        summary = section_body(read_text(path), "Resumo")
        if not summary:
            findings.append(Finding("WARNING", relative(root, path), "lista sem estado em ## Resumo"))
    return findings


def load_sync_module(root: Path):
    script = root / ".pi" / "scripts" / "sync_derived_views.py"
    spec = importlib.util.spec_from_file_location("sync_derived_views", script)
    if spec is None or spec.loader is None:
        raise RuntimeError("não foi possível carregar sync_derived_views.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def check_derived_views(root: Path, today: dt.date) -> list[Finding]:
    try:
        sync = load_sync_module(root)
        expected_home, expected_reviews, warnings = sync.build_outputs(root, today)
    except (OSError, UnicodeError, RuntimeError, ValueError) as exc:
        return [Finding("ERROR", ".pi/scripts/sync_derived_views.py", f"falha ao calcular visões derivadas: {exc}")]

    findings = [Finding("ERROR", "01_TOPICS", warning) for warning in warnings]
    for path, expected in (
        (root / "00_HOME.md", expected_home),
        (root / "02_REVIEWS" / "REVIEWS.md", expected_reviews),
    ):
        if not path.exists() or read_text(path) != expected:
            findings.append(Finding("ERROR", relative(root, path), "visão derivada divergente das fontes"))
    return findings


def run_checks(root: Path, today: dt.date) -> list[Finding]:
    findings = []
    findings.extend(check_topic_pairs(root))
    findings.extend(check_user_notes(root))
    findings.extend(check_wiki_links(root))
    findings.extend(check_exercise_state(root))
    findings.extend(check_derived_views(root, today))
    return sorted(findings, key=lambda item: (item.severity != "ERROR", item.path, item.message))


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    try:
        today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
        findings = run_checks(root, today)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Vault health failed: {exc}", file=sys.stderr)
        return 2

    if not findings:
        print("Vault health: OK")
        return 0
    for finding in findings:
        print(f"{finding.severity}: {finding.path}: {finding.message}")
    errors = sum(finding.severity == "ERROR" for finding in findings)
    warnings = len(findings) - errors
    print(f"Summary: {errors} error(s), {warnings} warning(s)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
