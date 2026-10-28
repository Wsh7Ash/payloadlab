# Changelog

All notable changes to `payloadlab` are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [SemVer](https://semver.org/).

## [1.0.0] - 2026-10-27

### Added

- Initial release: 50 unique proof-of-concept authoring skills across six phases
  (`scope`, `hypothesis`, `craft`, `deliver`, `observe`, `report`).
- Validator with structural, strength and hygiene rules; `50/50 skills valid`
  gate with `--json` output for CI.
- Deterministic renderer and `build` command writing `skills/`,
  `pack.json` (SHA-256 per skill) and `results/`.
- CLI: `validate`, `list`, `show`, `search`, `build`, `poc`.
- `poc` — structured test brief to phase-ordered PoC runbook with
  thin-coverage warnings.
- Test suite (17 tests) covering corpus shape, rules, regeneration, drift and
  every CLI command.
- CI workflow, docs (`ARCHITECTURE`, `USAGE`, `PROJECT_SPEC`), `SECURITY.md`.
