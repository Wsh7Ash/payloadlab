# Results

Reproducible evidence for the claims in `README.md`.

## Environment

- OS: Windows (MSYS2 shell), Python 3.14
- Runtime: Python 3.10+ standard library, `pytest` as dev dependency
- Dependency manager: `pip` in a clean venv (`python -m venv`)
- Network: none required at any point

## Validation performed

| Gate | Result |
|---|---|
| install (`pip install -e ".[dev]"` in a clean venv) | PASS |
| console script (`payloadlab validate` from the venv) | PASS |
| build (`payloadlab build`) | PASS (exit 0) |
| validation gate (`payloadlab validate`) | PASS — **50/50 skills valid** |
| unit tests (`pytest -q`) | PASS — **17 passed** (same suite also green from the venv) |
| demo run (`poc`, `search`, `list --phase`) | PASS |
| secret scan | PASS (0 real matches; the only grep hit is this file quoting the scan pattern) |

## Commands executed

```shell
export PYTHONPATH=src
python -m payloadlab build                    # regenerates skills/, pack.json, results/
python -m payloadlab validate                 # exit 0, prints 50/50
python -m pytest -q                           # 17 passed
python -m payloadlab poc --brief examples/demo-brief.json --top 24 > results/poc-demo.md
python -m payloadlab search marker control evidence --limit 5 > results/search-example.txt
grep -rInE "(ghp_|github_pat_|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY)" --exclude-dir=.git .
```

Clean-venv install (the system interpreter is externally managed under PEP 668):

```shell
python -m venv /tmp/pl-venv
/tmp/pl-venv/bin/python -m pip install -e ".[dev]"
/tmp/pl-venv/bin/payloadlab validate     # 50/50 skills valid
/tmp/pl-venv/bin/python -m pytest -q    # 17 passed
```

## Observed result

```
payloadlab: 50/50 skills valid
  ok  steps>=6 signals>=4 patterns>=3 pitfalls>=3 words>=180 refs canonical https
```

```
# PoC runbook - Reflected input observed in an attribute context
Context: html-attribute reflected search parameter on a member-only page   Skills matched: 38 of 50   Plan steps: 24

Thin coverage (no matched skill in these phases): observe, report
```

Phase distribution across the corpus:

```
scope 8, hypothesis 8, craft 9, deliver 8, observe 8, report 9  = 50
```

`pytest -q` reports `17 passed` with no warnings, both from the working tree and from the clean venv install. Secret scan returns no real matches.

## Generated artifacts

- `results/catalog.md` — the 50-skill index table
- `results/validation.json` — machine-readable gate report
- `results/poc-demo.md` — runbook produced from `examples/demo-brief.json`
- `results/search-example.txt` — keyword ranking output
- `pack.json` — manifest with a SHA-256 per skill file

## Known limitations

- The system Python is externally managed (PEP 668), so `pip install -e .` fails there by design; the venv run above is the install evidence.
- `poc` ranks by vocabulary substring overlap. It is a planning aid, not an analysis engine: it orders skills against a brief but never decides what to test.
- The demo brief scores strongly in `scope`/`hypothesis` and shows thin coverage in `observe`/`report` — expected for a 24-step cap; raising `--top` extends coverage.
- The word floor is a floor, not a quality guarantee: content judgment remains a reviewer's job.
