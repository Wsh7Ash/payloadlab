# Architecture

## Goals

1. **One source of truth.** Skills are authored as Python data; Markdown files are generated. A test asserts committed files match a fresh render, so the two can never disagree.
2. **Validation is a first-class gate.** Every quality floor lives in `validate.py` and is enforced by both the CLI and the test suite.
3. **No runtime dependencies.** Standard library only, so the pack runs anywhere Python 3.10+ exists.

## Components

```text
src/payloadlab/
├─ corpus/           authored skill data (source of truth)
│  ├─ __init__.py    PACK metadata + loads part1..part3
│  ├─ part1.py       skills 1-16   (scope, hypothesis)
│  ├─ part2.py       skills 17-33  (craft, deliver)
│  └─ part3.py       skills 34-50  (observe, report)
├─ model.py          Skill dataclass + strict dict loading
├─ render.py         deterministic SKILL.md + pack.json + results writer
├─ validate.py       every rule, one place
└─ cli.py            validate / list / show / search / build / poc
```

### Data flow

```text
part1..part3 (dicts)
      │  skill_from_dict()  -- shape check, rejects missing/empty fields
      ▼
   Skill (frozen dataclass)
      │
      ├─ validate_pack()  ─▶ Issue list ─▶ CLI exit code (0 only at 50/50)
      └─ render_skill()   ─▶ skills/<slug>/SKILL.md  (byte-deterministic)

poc (brief.json)
      │  score corpus against the brief's vocabulary (context, weakness, constraints, tags)
      ▼
   phase-ordered runbook  (scope → hypothesis → craft → deliver → observe → report)
      with thin-coverage warnings for phases that matched nothing
```

### The poc command

`poc` is payloadlab's domain command and separates this pack from a document library. It consumes a small test brief:

```json
{
  "title": "Reflected input observed in an attribute context",
  "context": "html-attribute reflected search parameter",
  "weakness": "CWE-79 ...",
  "constraints": ["authorized-scope only", "read-only evidence"],
  "tags": ["xss", "reflection"]
}
```

Vocabulary is aggregated across every field (tokens from context, weakness, constraints and tags, with hyphens and underscores normalised to spaces), then every skill is scored against that vocabulary by substring hits in slug, title, summary and tags. Matches are ordered by `PHASE_ORDER` and capped at `--top`, and phases with no matched skill are reported as thin coverage so an unaddressed part of the brief is visible rather than silent.

### Design decisions

- **`poc` is intentionally small.** It encodes vocabulary matching and phase ordering, not a proof strategy engine. What to prove and how far to go is judgment the reader keeps; the thin-coverage warning makes gaps explicit instead of guessing.
- **`scope` is the first phase by construction.** Because `PHASE_ORDER` begins with authorization and abort discipline, a plan always surfaces permission and safety skills before craft skills — the ordering itself encodes the pack's ethics.
- **Aggregation, not per-field matching.** The plan reflects the whole brief, not one line of it, so constraints and tags contribute equally with context.

### Validation layers

| Layer | Where | Enforces |
|---|---|---|
| Shape | `model.skill_from_dict` | required keys, non-empty entries, `(label, code)` pattern pairs |
| Skill rules | `validate.skill_issues` | slug/title format, summary/use/avoid length, description window, tag format, step/signal/pattern/pitfall/done floors (labels >= 8 chars), reference format, word floor, placeholder and local-path hygiene |
| Pack rules | `validate.pack_issues` | exact skill count (50), unique slugs and titles |
| Disk sync | `cli.cmd_validate` | committed `SKILL.md` matches a fresh render byte for byte |

The CLI exits `0` only when every layer passes, which is what "50/50 valid" means.