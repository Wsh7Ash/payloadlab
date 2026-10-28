---
name: blast-radius-budget
description: "Declare the maximum effect your proof is allowed to produce before you build it, so scale, writes and notifications stay inside a budget you chose rather than one the test discovered. Use when a proof could plausibly write data, notify users, consume quota or scale with input size"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [safety, planning, scope]
---

# Blast Radius Budget

> Declare the maximum effect your proof is allowed to produce before you build it, so scale, writes and notifications stay inside a budget you chose rather than one the test discovered

**Use when:** a proof could plausibly write data, notify users, consume quota or scale with input size

**Avoid when:** the proof only reads data you own and produces no side effects at all

## Procedure

1. Enumerate every side effect the proof could produce: writes, emails, queue jobs, quota use or third-party calls.
2. Assign each effect a hard ceiling: records touched, messages sent, requests issued, duration of load.
3. Choose ceilings that prove the claim at minimum scale, since one successful instance is usually enough.
4. Write the budget into the test record before running anything, so overrun is measurable rather than vague.
5. Monitor consumption during the test and stop at the ceiling even if the claim is not yet fully proven.
6. Record actual consumption against the budget so the next test starts from measured reality.

## Signals

- The proof scales with an input you control, such as list size, retry count or concurrency.
- A successful trigger would notify real users or enqueue work visible to operators.
- Your budget exists only in your head, which means there is no number to compare against.
- The claim feels almost proven, and one more larger run would settle it, which is exactly when budgets matter.

## Patterns

**1. Budget line**

```text
effect=write ceiling=5-records effect=notify ceiling=0 effect=requests ceiling=50 declared-before-run=yes
```

**2. Spend note**

```text
spent-writes=1 spent-notifies=0 spent-requests=14 verdict=inside-budget remaining=36
```

**3. Stop rule**

```text
trigger=ceiling-reached action=stop-and-record-partial-claim reason=budget-beats-completeness
```

## Pitfalls

- Declaring no budget and discovering the ceiling when production alerts fire.
- Setting a budget at a scale that cannot prove the claim, then quietly exceeding it once the run looks safe.
- Counting only request volume while ignoring notifications, writes and third-party calls.
- Raising the budget mid-test because the first attempt was inconclusive.

## Done when

- Every side effect has a declared ceiling written into the test record before execution.
- Actual consumption is recorded against the budget and the test stopped at or below it.
- An overrun, if any, is logged with what it produced and what it cost.

## References

- [OWASP - testing guidance for safe testing](https://owasp.org/www-project-web-security-testing-guide/)
- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
