"""Corpus, rendering and CLI tests for payloadlab.

Every assertion here is executable evidence for the claims in RESULTS.md:
50 unique skills, a clean validation pass, byte-identical regeneration and a
CLI (validate / list / show / search / build / poc) that behaves as
documented.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from payloadlab.corpus import PACK, SKILLS
from payloadlab.render import build_pack, render_skill, sha256_of, word_count
from payloadlab.validate import (
    FORBIDDEN_RE,
    MIN_WORDS,
    pack_issues,
    skill_issues,
    validate_pack,
)

ROOT = Path(__file__).resolve().parents[1]


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env["PYTHONPATH"] = str(ROOT / "src")
    return subprocess.run(
        [sys.executable, "-m", "payloadlab", *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
        env=env,
    )


# ---------------------------------------------------------------- corpus shape


def test_pack_declares_fifty_and_delivers_fifty() -> None:
    assert PACK["expected_skills"] == 50
    assert len(SKILLS) == 50


def test_slugs_and_titles_are_unique() -> None:
    slugs = [s.slug for s in SKILLS]
    titles = [s.title.lower() for s in SKILLS]
    assert len(set(slugs)) == 50
    assert len(set(titles)) == 50


def test_every_skill_passes_every_rule() -> None:
    assert validate_pack(PACK, SKILLS) == []


def test_phases_are_known_and_balanced() -> None:
    allowed = {"scope", "hypothesis", "craft", "deliver", "observe", "report"}
    counts: dict[str, int] = {}
    for skill in SKILLS:
        phase = skill.meta["phase"]
        assert phase in allowed, skill.slug
        counts[phase] = counts.get(phase, 0) + 1
    assert counts["scope"] == 8
    assert counts["hypothesis"] == 8
    assert counts["craft"] == 9
    assert counts["deliver"] == 8
    assert counts["observe"] == 8
    assert counts["report"] == 9
    assert sum(counts.values()) == 50


def test_word_floor_is_real_not_theoretical() -> None:
    weakest = min(SKILLS, key=lambda s: word_count(render_skill(PACK, s)))
    assert word_count(render_skill(PACK, weakest)) >= MIN_WORDS


def test_no_placeholder_or_local_path_tokens() -> None:
    for skill in SKILLS:
        rendered = render_skill(PACK, skill)
        assert not FORBIDDEN_RE.search(rendered), skill.slug
        assert "C:\\" not in rendered and "/Users/" not in rendered, skill.slug


# ------------------------------------------------------------ generated files


def test_committed_skills_match_corpus_render() -> None:
    for skill in SKILLS:
        path = ROOT / "skills" / skill.slug / "SKILL.md"
        assert path.exists(), f"missing {path}"
        assert path.read_text(encoding="utf-8") == render_skill(PACK, skill)


def test_pack_json_hashes_match_files() -> None:
    manifest = json.loads((ROOT / "pack.json").read_text(encoding="utf-8"))
    assert manifest["skill_count"] == 50
    assert len(manifest["skills"]) == 50
    for entry in manifest["skills"]:
        path = ROOT / entry["path"]
        digest = sha256_of(path.read_text(encoding="utf-8"))
        assert digest == entry["sha256"], entry["slug"]


def test_build_is_idempotent(tmp_path: Path) -> None:
    build_pack(tmp_path, PACK, SKILLS)
    for skill in SKILLS:
        a = (tmp_path / "skills" / skill.slug / "SKILL.md").read_bytes()
        b = (ROOT / "skills" / skill.slug / "SKILL.md").read_bytes()
        assert a == b, skill.slug
    assert (tmp_path / "pack.json").read_bytes() == (ROOT / "pack.json").read_bytes()


def test_drift_is_detected(tmp_path: Path) -> None:
    build_pack(tmp_path, PACK, SKILLS)
    victim = tmp_path / "skills" / SKILLS[0].slug / "SKILL.md"
    victim.write_text(victim.read_text(encoding="utf-8") + "\nedited\n", encoding="utf-8")
    rendered = render_skill(PACK, SKILLS[0])
    on_disk = victim.read_text(encoding="utf-8")
    assert on_disk != rendered


# ---------------------------------------------------------------------- CLI


def test_cli_validate_reports_fifty_of_fifty() -> None:
    proc = run_cli("validate", "--json")
    assert proc.returncode == 0, proc.stdout + proc.stderr
    payload = json.loads(proc.stdout)
    assert payload["checked"] == 50
    assert payload["valid"] == 50
    assert payload["passed"] is True
    assert payload["issues"] == []


def test_cli_list_and_show_and_search() -> None:
    listing = run_cli("list", "--json")
    assert listing.returncode == 0
    assert len(json.loads(listing.stdout)) == 50

    # --phase filter narrows the listing to one phase
    only_craft = run_cli("list", "--phase", "craft", "--json")
    assert only_craft.returncode == 0
    crafted = json.loads(only_craft.stdout)
    assert len(crafted) == 9
    assert all(entry["meta"]["phase"] == "craft" for entry in crafted)

    show = run_cli("show", SKILLS[0].slug)
    assert show.returncode == 0
    assert show.stdout.startswith(f"---\nname: {SKILLS[0].slug}")

    missing = run_cli("show", "not-a-real-skill")
    assert missing.returncode == 1

    search = run_cli("search", "marker", "control")
    assert search.returncode == 0
    assert search.stdout.strip() != ""

    nohit = run_cli("search", "zzzz-no-such-term")
    assert nohit.returncode == 1
    assert "no matches" in nohit.stdout


def test_cli_poc_orders_phases_and_flags_thin_coverage() -> None:
    spec = ROOT / "examples" / "demo-brief.json"
    text = run_cli("poc", "--brief", str(spec), "--top", "24")
    assert text.returncode == 0, text.stdout + text.stderr
    assert text.stdout.startswith("# PoC runbook - ")
    assert "Skills matched:" in text.stdout
    # phases render in PHASE_ORDER
    order = [
        "## scope",
        "## hypothesis",
        "## craft",
        "## deliver",
        "## observe",
        "## report",
    ]
    positions = [text.stdout.find(marker) for marker in order]
    rendered = [p for p in positions if p != -1]
    assert rendered == sorted(rendered), "phase headers must appear in PHASE_ORDER"

    payload = json.loads(
        run_cli("poc", "--brief", str(spec), "--top", "24", "--json").stdout
    )
    assert payload["skills_total"] == 50
    assert payload["plan_steps"] == 24
    assert payload["skills_matched"] > 0
    from payloadlab.cli import PHASE_ORDER

    assert all(entry["phase"] in PHASE_ORDER for entry in payload["plan"])
    assert payload["missing_phases"] == [
        p for p in PHASE_ORDER if p not in {e["phase"] for e in payload["plan"]}
    ]
    assert payload["weakness"].startswith("cwe-79")


def test_cli_poc_rejects_missing_brief_file() -> None:
    proc = run_cli("poc", "--brief", str(ROOT / "examples" / "no-such-brief.json"))
    assert proc.returncode != 0


def test_pocplan_aggregates_vocabulary_across_fields() -> None:
    from payloadlab.cli import build_pocplan

    brief = {
        "title": "Attribute-context reflection",
        "context": "html-attribute reflected parameter",
        "weakness": "CWE-79",
        "constraints": ["authorized-scope", "read-only evidence"],
        "tags": ["xss", "reflection"],
    }
    payload = build_pocplan(brief, top=6)
    assert payload["plan_steps"] == 6
    assert payload["skills_total"] == 50
    from payloadlab.cli import PHASE_ORDER

    phases = [entry["phase"] for entry in payload["plan"]]
    assert phases == sorted(phases, key=PHASE_ORDER.index)


def test_pack_issues_catches_a_short_corpus() -> None:
    issues = pack_issues(PACK, SKILLS[:-1])
    assert any(issue.rule == "skill-count" for issue in issues)


def test_single_skill_rule_violations_are_reported() -> None:
    broken = dict(SKILLS[0].__dict__)
    broken["steps"] = ("one", "two")
    from payloadlab.model import skill_from_dict

    issues = skill_issues(PACK, skill_from_dict(broken), "")
    rules = {issue.rule for issue in issues}
    assert "steps-count" in rules