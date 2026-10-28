---
name: test-data-selection-discipline
description: "Choose test records that are synthetic, identifiable as yours and isolated from real users, so the proof never depends on, exposes or disturbs somebody else's data. Use when the proof needs existing rows, files, orders or records to operate on"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [test-data, safety, setup]
---

# Test Data Selection Discipline

> Choose test records that are synthetic, identifiable as yours and isolated from real users, so the proof never depends on, exposes or disturbs somebody else's data

**Use when:** the proof needs existing rows, files, orders or records to operate on

**Avoid when:** the proof runs entirely against objects your own test accounts just created

## Procedure

1. Prefer records your test identities created in this session, since ownership and content are both known.
2. Where seeded data is required, confirm its provenance and that no real person's information is present.
3. Tag every record you select with a marker so later review can distinguish test data from live data.
4. Never select a record at random from production without knowing exactly whose it is and what it contains.
5. Record which records the proof touched, so cleanup and disclosure questions can be answered precisely.
6. Re-verify selection at execution time, because record sets shift between planning and running.

## Signals

- The fastest path is to pick any row from production, which guarantees someone's real data is involved.
- Selected records were created by someone else and their content is unknown to you.
- No marker distinguishes your test records from live ones during cleanup or evidence review.
- Record identifiers changed since planning, so the selection list is silently stale.

## Patterns

**1. Selection row**

```text
record=order-4471 owner=test-a source=self-created marker=lab-01 contains-pii=no status=approved
```

**2. Provenance note**

```text
seed=fixture-import rows=50 provenance=synthetic last-verified=2026-10-27 contains-pii=no
```

**3. Touch log**

```text
touched=[order-4471,order-4472] created-by=test-a cleanup=restore-or-delete-after-run owner=you
```

## Pitfalls

- Sampling a production row because it was convenient, then reading real user data you had no reason to touch.
- Assuming seeded data is synthetic without checking its provenance.
- Selecting records without markers, so cleanup cannot tell test rows from live rows.
- Never logging what was touched, which makes both cleanup and disclosure answers guesses.

## Done when

- Every record used is self-created or verified synthetic, with provenance recorded.
- Each selected record carries a marker distinguishing it from live data.
- A touch log lists exactly what the proof operated on, ready for cleanup.

## References

- [OWASP - testing guidance for test data handling](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
