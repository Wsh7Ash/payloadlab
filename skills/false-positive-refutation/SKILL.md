---
name: false-positive-refutation
description: "Attempt to disprove your own observation before reporting it, because a claim that survives your strongest counter-attempt needs no defense against a reviewer's. Use when the observation is captured and the finding is about to be written"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [rigor, observe, quality]
---

# False Positive Refutation

> Attempt to disprove your own observation before reporting it, because a claim that survives your strongest counter-attempt needs no defense against a reviewer's

**Use when:** the observation is captured and the finding is about to be written

**Avoid when:** the evidence is mechanical, such as another user's record appearing in your session

## Procedure

1. List every way the observation could be a false positive: artifacts, state, cache or your own client.
2. Design and run the cheapest test that would show each explanation to be true.
3. Attempt to reproduce the negative case, confirming the system behaves correctly without your variable.
4. Attack your own attribution, checking the effect could not have come from another cause.
5. Record which refutation attempts were run and what each returned.
6. Report the finding only with its surviving refutations listed, which is what makes it credible.

## Signals

- You have not tried once to make your own finding fall apart, which a reviewer will do for you.
- A cache or stale-state explanation fits the observation and remains untested.
- The negative case was never run, so normal behavior is assumed rather than shown.
- You feel resistant to testing the finding, which is precisely when the test matters most.

## Patterns

**1. Refute row**

```text
attempt=cache-explanation result=refuted-via-cache-bust attempt=shared-state result=refuted-via-clean-session
```

**2. Negative run**

```text
condition=no-variable observed=expected-behavior confidence-in-finding=increased note=attached
```

**3. Survivor list**

```text
refutations-run=4 refuted=4 surviving-challenges=0 residual-risk=undocumented-concurrent-load
```

## Pitfalls

- Testing only the explanations that would be easy to dismiss, leaving hard ones untouched.
- Skipping the negative case, so normal behavior is asserted instead of demonstrated.
- Never attempting attribution attacks, so a coincidental cause survives into the report.
- Omitting surviving challenges from the report, handing the reviewer your own best counter-argument.

## Done when

- Candidate false-positive explanations are listed with a refutation run for each.
- The negative case has been demonstrated under the same conditions.
- Surviving challenges are disclosed in the report alongside the evidence.

## References

- [OWASP - testing guidance for false positives](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
