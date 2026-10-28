---
name: rival-explanation-elimination
description: "List the innocent explanations for your observation and test each one, so the finding rests on eliminating alternatives rather than on the first story that fit. Use when an observation matches your hypothesis but could plausibly have other causes"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [rigor, hypothesis, validation]
---

# Rival Explanation Elimination

> List the innocent explanations for your observation and test each one, so the finding rests on eliminating alternatives rather than on the first story that fit

**Use when:** an observation matches your hypothesis but could plausibly have other causes

**Avoid when:** the mechanism is directly observable, such as a response echoing another user's record

## Procedure

1. Write down every plausible alternative explanation for the observation, including boring ones.
2. For each rival, name a test that would distinguish it from your hypothesis.
3. Run the cheapest distinguishing tests first, since one may resolve the question immediately.
4. Record which rivals were eliminated with evidence and which remain standing.
5. State remaining rivals in the report if any survive, which strengthens rather than weakens it.
6. Revisit survivors if later evidence changes, since a leftover rival can invalidate the whole claim.

## Signals

- One story fits the observation and you stopped looking once it did.
- Shared state between test accounts could explain a result you are calling an isolation failure.
- Cached, stale or delayed data offers an obvious innocent explanation nobody checked.
- No rival was written down, so the report cannot show alternatives were considered.

## Patterns

**1. Rival table**

```text
rival=shared-team eliminated=yes evidence=no-shared-group rival=cache-stale eliminated=yes evidence=cache-bust-passed
```

**2. Survivor note**

```text
rival=async-delay status=standing test=wait-30s-and-recheck owner=you
```

**3. Report line**

```text
claim=cross-tenant-read rivals-tested=4 rivals-eliminated=4 survivors=none confidence=high
```

## Pitfalls

- Accepting the first coherent narrative, which is a reasoning failure rather than an analysis.
- Testing only rivals that would be convenient to eliminate.
- Leaving survivors unmentioned in the report, so a reviewer discovers them instead of you.
- Ignoring shared-state rivals, the most common innocent explanation in multi-account tests.

## Done when

- Plausible rivals are listed with a distinguishing test defined for each.
- Rivals are marked eliminated with evidence or standing with a next test.
- Any surviving rival is disclosed in the report.

## References

- [OWASP - testing guidance for validation](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
