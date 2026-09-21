from __future__ import annotations

import datetime as dt
import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


sync = load_module("test_sync_derived_views", REPO_ROOT / ".pi" / "scripts" / "sync_derived_views.py")
health = load_module(
    "test_check_vault",
    REPO_ROOT / ".pi" / "skills" / "vault-health" / "scripts" / "check_vault.py",
)


def topic_text(name: str, next_review: str, status: str = "Praticando", level: str = "3") -> str:
    return f"""# {name}

Data criação: 2026-09-01
Data último estudo: 2026-09-10
Data última revisão:
Data próxima revisão: {next_review}
Status: {status}
Nível: {level}

## Conteúdo

## Gaps

## Erros

## Minhas anotações

<!-- USER-NOTES:START -->

<!-- USER-NOTES:END -->
"""


class VaultFixture:
    def __init__(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "01_TOPICS").mkdir()
        (self.root / "02_REVIEWS").mkdir()
        (self.root / "03_PROJECTS").mkdir()
        (self.root / "05_EXERCISES").mkdir()
        (self.root / ".pi" / "scripts").mkdir(parents=True)
        shutil.copy2(
            REPO_ROOT / ".pi" / "scripts" / "sync_derived_views.py",
            self.root / ".pi" / "scripts" / "sync_derived_views.py",
        )
        (self.root / "00_HOME.md").write_text(
            "# Active Study System\n\nTexto preservado.\n", encoding="utf-8"
        )

    def add_topic(self, name: str, next_review: str, status: str = "Praticando", level: str = "3") -> Path:
        folder = self.root / "01_TOPICS" / name
        folder.mkdir()
        main = folder / f"{name}.md"
        main.write_text(topic_text(name, next_review, status, level), encoding="utf-8")
        (folder / f"Perguntas sobre {name}.md").write_text(
            f"# Perguntas sobre {name}\n\nData criação: 2026-09-01\n", encoding="utf-8"
        )
        return main

    def sync(self, today: dt.date) -> None:
        home, reviews, _ = sync.build_outputs(self.root, today)
        (self.root / "00_HOME.md").write_text(home, encoding="utf-8")
        (self.root / "02_REVIEWS" / "REVIEWS.md").write_text(reviews, encoding="utf-8")

    def close(self) -> None:
        self.temp.cleanup()


class SyncDerivedViewsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = VaultFixture()
        self.today = dt.date(2026, 9, 20)

    def tearDown(self) -> None:
        self.fixture.close()

    def test_groups_overdue_today_and_future_and_preserves_home_text(self) -> None:
        self.fixture.add_topic("Atrasado", "2026-09-19")
        self.fixture.add_topic("Hoje", "2026-09-20")
        self.fixture.add_topic("Futuro", "2026-09-21")

        home, reviews, warnings = sync.build_outputs(self.fixture.root, self.today)
        topics, _ = sync.collect_topics(self.fixture.root)
        overdue, due_today, upcoming = sync.review_groups(topics, self.today)

        self.assertEqual([], warnings)
        self.assertEqual(["Atrasado"], [topic.name for topic in overdue])
        self.assertEqual(["Hoje"], [topic.name for topic in due_today])
        self.assertEqual(["Futuro"], [topic.name for topic in upcoming])
        self.assertIn("Texto preservado.", home)
        self.assertIn("## Revisões pendentes", home)
        self.assertIn("Atrasado", home)
        self.assertIn("Hoje", home)
        self.assertIn("## Atrasadas\n\n- [[01_TOPICS/Atrasado", reviews)
        self.assertIn("## Hoje\n\n- [[01_TOPICS/Hoje", reviews)
        self.assertIn("## Próximas\n\n- [[01_TOPICS/Futuro", reviews)

    def test_output_is_idempotent_and_reports_invalid_date(self) -> None:
        self.fixture.add_topic("Inválido", "20-09-2026")
        first_home, first_reviews, warnings = sync.build_outputs(self.fixture.root, self.today)
        (self.fixture.root / "00_HOME.md").write_text(first_home, encoding="utf-8")
        (self.fixture.root / "02_REVIEWS" / "REVIEWS.md").write_text(first_reviews, encoding="utf-8")
        second_home, second_reviews, _ = sync.build_outputs(self.fixture.root, self.today)

        self.assertEqual(first_home, second_home)
        self.assertEqual(first_reviews, second_reviews)
        self.assertEqual(1, len(warnings))
        self.assertIn("inválida", warnings[0])


class VaultHealthTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = VaultFixture()
        self.today = dt.date(2026, 9, 20)

    def tearDown(self) -> None:
        self.fixture.close()

    def test_healthy_fixture_has_no_findings(self) -> None:
        self.fixture.add_topic("Saudável", "2026-09-21")
        self.fixture.sync(self.today)
        original_home = (self.fixture.root / "00_HOME.md").read_text(encoding="utf-8")
        original_reviews = (self.fixture.root / "02_REVIEWS" / "REVIEWS.md").read_text(encoding="utf-8")

        self.assertEqual([], health.run_checks(self.fixture.root, self.today))
        self.assertEqual(original_home, (self.fixture.root / "00_HOME.md").read_text(encoding="utf-8"))
        self.assertEqual(
            original_reviews,
            (self.fixture.root / "02_REVIEWS" / "REVIEWS.md").read_text(encoding="utf-8"),
        )

    def test_detects_structural_state_protection_link_exercise_and_drift_errors(self) -> None:
        main = self.fixture.add_topic("Quebrado", "2026-09-21", status="Inexistente", level="9")
        (main.parent / "Perguntas sobre Quebrado.md").unlink()
        main.write_text(
            main.read_text(encoding="utf-8").replace("<!-- USER-NOTES:END -->", "")
            + "\n[[01_TOPICS/Ausente/Ausente]]\n",
            encoding="utf-8",
        )
        exercise = self.fixture.root / "05_EXERCISES" / "Quebrado" / "lista.md"
        exercise.parent.mkdir()
        exercise.write_text("# Lista\n\n## Resumo\n", encoding="utf-8")
        self.fixture.sync(self.today)
        (self.fixture.root / "00_HOME.md").write_text("# divergente\n", encoding="utf-8")

        findings = health.run_checks(self.fixture.root, self.today)
        messages = "\n".join(finding.message for finding in findings)

        self.assertIn("arquivo de perguntas ausente", messages)
        self.assertIn("Status inválido", messages)
        self.assertIn("Nível inválido", messages)
        self.assertIn("marcadores USER-NOTES", messages)
        self.assertIn("link canônico quebrado", messages)
        self.assertIn("lista sem estado", messages)
        self.assertIn("visão derivada divergente", messages)


if __name__ == "__main__":
    unittest.main()
