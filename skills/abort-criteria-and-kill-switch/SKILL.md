---
name: abort-criteria-and-kill-switch
description: "Define in advance the exact observations that mean stop testing now, and prepare the action that stops it, so aborting is a rehearsed move rather than a decision made under pressure. Use when the test can produce side effects, touch shared systems or run long enough for conditions to change"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [safety, planning, sre]
---

# Abort Criteria and Kill Switch

> Define in advance the exact observations that mean stop testing now, and prepare the action that stops it, so aborting is a rehearsed move rather than a decision made under pressure

**Use when:** the test can produce side effects, touch shared systems or run long enough for conditions to change

**Avoid when:** the proof is a single read-only request executed in one shot

## Procedure

1. List observable conditions that require an immediate stop: error spikes, alerts, user-visible impact or scope drift.
2. Write each condition as a checkable statement with the signal you would actually see.
3. Prepare the stop action itself: the command, the toggle, the request that halts the test cleanly.
4. Verify the stop action works before the test starts, because an untested kill switch is a hope.
5. Put the abort criteria where you will see them mid-test, not buried in the plan document.
6. Run the test only while you can act on an abort within a stated reaction time.

## Signals

- The plan lists success conditions but no stop conditions, which means nothing tells you when to halt.
- The kill switch has never been exercised, so its behavior during an incident is unknown.
- Alerts during the test would arrive somewhere you are not watching.
- Conditions changed since planning, and the original abort criteria no longer match reality.

## Patterns

**1. Abort list**

```text
stop=error-rate-spike stop=user-complaint stop=scope-drift stop=blast-budget-exceeded reaction=immediate
```

**2. Kill line**

```text
action=cancel-running-job verified=2026-10-27 verified-by=dry-run time-to-stop=3s owner=you
```

**3. Watch rule**

```text
monitor=alerts-channel during-test=yes reaction-time=1-minute unattended-test=forbidden
```

## Pitfalls

- Writing abort criteria nobody reviews while the test is running.
- Assuming a kill switch works because it existed in the design, not because you pressed it.
- Setting conditions so vague that any observation can be argued either way.
- Running unattended, which makes every abort criterion theoretical.

## Done when

- Every stop condition is written as a checkable observation with the signal named.
- The kill switch has been verified before the test, and its verification is recorded.
- The test runs only while someone can react within the stated time.

## References

- [OWASP - testing guidance for safe testing](https://owasp.org/www-project-web-security-testing-guide/)
- [CISA - coordinated vulnerability disclosure guidance](https://www.cisa.gov/coordinated-vulnerability-disclosure-process)
