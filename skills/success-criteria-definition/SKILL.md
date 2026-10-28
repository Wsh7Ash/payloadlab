---
name: success-criteria-definition
description: "Define what counts as demonstrated before running the proof, with concrete observable thresholds, so the test has a finish line that cannot move after the results are in. Use when proof work begins and done is still a feeling rather than a defined observation"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [hypothesis, rigor, planning]
---

# Success Criteria Definition

> Define what counts as demonstrated before running the proof, with concrete observable thresholds, so the test has a finish line that cannot move after the results are in

**Use when:** proof work begins and done is still a feeling rather than a defined observation

**Avoid when:** the program's report template already specifies the exact evidence required

## Procedure

1. Write the primary observation that would demonstrate the claim, in concrete checkable terms.
2. Set a threshold where quantity matters, such as records returned or action completed.
3. Distinguish minimum proof from ideal proof, so the test knows when it may stop.
4. Define what would count as failure or inconclusive, not only what counts as success.
5. Record criteria with the hypothesis before execution so results are judged against a fixed bar.
6. Resist lowering the bar mid-test; instead record an inconclusive result and revise openly.

## Signals

- Success is described as confirming the issue with no observable specified.
- The bar was quietly lowered after a partial result, which converts a miss into a claim.
- No inconclusive category exists, forcing every outcome into success or failure.
- Minimum proof and ideal proof are conflated, so the test ran far past what was needed.

## Patterns

**1. Criteria line**

```text
primary=200-with-3-owned-fields minimum=200-with-1-owned-field ideal=cross-tenant-list failure=403-or-empty
```

**2. Stop rule**

```text
met=minimum stop=yes note=record-as-demonstrated-not-exhaustive
```

**3. Revision**

```text
v1=needs-full-list v2=one-record-sufficient reason=minimum-proven logged=2026-10-27 no-lowering=acknowledged
```

## Pitfalls

- Defining success after seeing results, which guarantees the test succeeds.
- Having no inconclusive outcome, which pressures partial data into a claim.
- Running to ideal proof when minimum proof already demonstrated the risk.
- Leaving thresholds verbal, so the reviewer cannot check them against the evidence.

## Done when

- Success, minimum and failure observations are written concretely before execution.
- The test stopped at a declared threshold or recorded why it continued.
- Any criterion change is dated and openly marked as a revision.

## References

- [OWASP - testing guidance for acceptance criteria](https://owasp.org/www-project-web-security-testing-guide/)
- [FIRST - Common Vulnerability Scoring System](https://www.first.org/cvss/)
