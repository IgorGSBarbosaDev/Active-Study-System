"""Synchronize the derived Home and review agenda from Vault source notes."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path


HOME_SECTIONS = (
    ("Estudando", "ESTUDANDO"),
    ("Revisões pendentes", "REVISOES_PENDENTES"),
    ("Próximas revisões", "PROXIMAS_REVISOES"),
    ("Projetos ativos", "PROJETOS_ATIVOS"),
)
FIELDS = {"Data próxima revisão", "Data último estudo", "Status", "Nível"}
COMPLETED_PROJECT_STATUSES = {
    "concluido",
    "concluida",
    "arquivado",
    "arquivada",
    "completed",
    "archived",
}


@dataclass(frozen=True)
class Topic:
    name: str
    path: Path
    link: str
    status: str
    level: str
    last_study: str
    next_review: str
    next_review_date: dt.date | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--date", help="Current date in YYYY-MM-DD; defaults to local date.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^\s*([^:]+):\s*(.*?)\s*$", line)
        if match and match.group(1) in FIELDS:
            fields[match.group(1)] = match.group(2)
    return fields


def parse_date(value: str) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def heading(path: Path) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", read_text(path), flags=re.MULTILINE)
    return match.group(1).strip() if match else path.stem


def wiki_link(root: Path, path: Path, label: str) -> str:
    relative = path.relative_to(root).with_suffix("").as_posix()
    return f"[[{relative}|{label}]]"


def collect_topics(root: Path) -> tuple[list[Topic], list[str]]:
    topics_root = root / "01_TOPICS"
    topics: list[Topic] = []
    warnings: list[str] = []
    if not topics_root.exists():
        return topics, warnings

    for topic_dir in sorted(
        (item for item in topics_root.iterdir() if item.is_dir()),
        key=lambda path: path.name.casefold(),
    ):
        main = topic_dir / f"{topic_dir.name}.md"
        if not main.exists():
            continue
        fields = parse_fields(read_text(main))
        raw_date = fields.get("Data próxima revisão", "")
        parsed_date = parse_date(raw_date)
        if raw_date and parsed_date is None:
            warnings.append(f"{main.relative_to(root)}: Data próxima revisão inválida ({raw_date})")
        topics.append(
            Topic(
                name=topic_dir.name,
                path=main,
                link=wiki_link(root, main, topic_dir.name),
                status=fields.get("Status", ""),
                level=fields.get("Nível", ""),
                last_study=fields.get("Data último estudo", ""),
                next_review=raw_date,
                next_review_date=parsed_date,
            )
        )
    return topics, warnings


def review_groups(
    topics: list[Topic], today: dt.date
) -> tuple[list[Topic], list[Topic], list[Topic]]:
    overdue = sorted(
        (topic for topic in topics if topic.next_review_date and topic.next_review_date < today),
        key=lambda topic: (topic.next_review_date, topic.name.casefold()),
    )
    due_today = sorted(
        (topic for topic in topics if topic.next_review_date == today),
        key=lambda topic: topic.name.casefold(),
    )
    upcoming = sorted(
        (topic for topic in topics if topic.next_review_date and topic.next_review_date > today),
        key=lambda topic: (topic.next_review_date, topic.name.casefold()),
    )
    return overdue, due_today, upcoming


def topic_lines(topics: list[Topic], empty: str) -> str:
    lines = [f"- {topic.link} — {topic.next_review}" for topic in topics]
    return "\n".join(lines) if lines else f"- {empty}"


def render_studying(topics: list[Topic]) -> str:
    studying = sorted(
        (topic for topic in topics if topic.status in {"Estudando", "Praticando"}),
        key=lambda topic: topic.name.casefold(),
    )
    lines: list[str] = []
    for topic in studying:
        details = [topic.status]
        if topic.level:
            details.append(f"Nível {topic.level}")
        if topic.last_study:
            details.append(f"último estudo {topic.last_study}")
        lines.append(f"- {topic.link} — {' · '.join(details)}")
    return "\n".join(lines) if lines else "- Nenhum tópico em estudo."


def collect_projects(root: Path) -> str:
    projects_root = root / "03_PROJECTS"
    if not projects_root.exists():
        return "- Nenhum projeto ativo."
    projects: list[tuple[str, str]] = []
    for path in projects_root.rglob("*.md"):
        if path.name.casefold() == "readme.md":
            continue
        status = parse_fields(read_text(path)).get("Status", "").strip().casefold()
        if status in COMPLETED_PROJECT_STATUSES:
            continue
        title = heading(path)
        projects.append((title.casefold(), f"- {wiki_link(root, path, title)}"))
    projects.sort()
    return "\n".join(line for _, line in projects) or "- Nenhum projeto ativo."


def replace_managed_block(text: str, heading_text: str, key: str, content: str) -> str:
    start = f"<!-- DERIVED:START:{key} -->"
    end = f"<!-- DERIVED:END:{key} -->"
    generated = f"{start}\n{content.rstrip()}\n{end}\n"
    section = re.compile(
        rf"^(##\s+{re.escape(heading_text)}\s*$)(.*?)(?=^##\s+|\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )
    match = section.search(text)
    if match is None:
        separator = "" if not text or text.endswith("\n") else "\n"
        return f"{text}{separator}\n## {heading_text}\n\n{generated}"
    body = match.group(2)
    any_managed = re.compile(
        r"<!-- (?:UPDATE-HOME|DERIVED):START:[A-Z_]+ -->.*?"
        r"<!-- (?:UPDATE-HOME|DERIVED):END:[A-Z_]+ -->",
        flags=re.DOTALL,
    )
    new_body = (
        any_managed.sub(generated.rstrip("\n"), body, count=1)
        if any_managed.search(body)
        else f"\n{generated}{body}"
    )
    return text[: match.start(2)] + new_body + text[match.end(2) :]


def build_home(root: Path, topics: list[Topic], today: dt.date) -> str:
    home_path = root / "00_HOME.md"
    text = read_text(home_path) if home_path.exists() else "# Active Study System\n"
    text = re.sub(r"^## Revisões de hoje\s*$", "## Revisões pendentes", text, flags=re.MULTILINE)
    overdue, due_today, upcoming = review_groups(topics, today)
    pending = overdue + due_today
    contents = {
        "ESTUDANDO": render_studying(topics),
        "REVISOES_PENDENTES": topic_lines(pending, "Nenhuma revisão pendente."),
        "PROXIMAS_REVISOES": topic_lines(upcoming, "Nenhuma revisão futura."),
        "PROJETOS_ATIVOS": collect_projects(root),
    }
    for section_heading, key in HOME_SECTIONS:
        text = replace_managed_block(text, section_heading, key, contents[key])
    return text.rstrip() + "\n"


def build_reviews(topics: list[Topic], today: dt.date) -> str:
    overdue, due_today, upcoming = review_groups(topics, today)
    return (
        "# Revisões\n\n"
        "## Atrasadas\n\n"
        f"{topic_lines(overdue, 'Nenhuma.')}\n\n"
        "## Hoje\n\n"
        f"{topic_lines(due_today, 'Nenhuma.')}\n\n"
        "## Próximas\n\n"
        f"{topic_lines(upcoming, 'Nenhuma.')}\n"
    )


def build_outputs(root: Path, today: dt.date) -> tuple[str, str, list[str]]:
    topics, warnings = collect_topics(root)
    return build_home(root, topics, today), build_reviews(topics, today), warnings


def write_text(path: Path, content: str) -> bool:
    current = read_text(path) if path.exists() else None
    if current == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    try:
        today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
        home, reviews, warnings = build_outputs(root, today)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Synchronization failed: {exc}", file=sys.stderr)
        return 1

    if args.dry_run:
        print("===== 00_HOME.md =====")
        print(home, end="")
        print("===== 02_REVIEWS/REVIEWS.md =====")
        print(reviews, end="")
    else:
        changed = []
        if write_text(root / "00_HOME.md", home):
            changed.append("00_HOME.md")
        if write_text(root / "02_REVIEWS" / "REVIEWS.md", reviews):
            changed.append("02_REVIEWS/REVIEWS.md")
        print("Synchronized: " + (", ".join(changed) if changed else "no changes"))

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
