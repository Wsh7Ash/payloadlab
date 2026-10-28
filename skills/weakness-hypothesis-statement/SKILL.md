---
name: weakness-hypothesis-statement
description: "Write the proof's hypothesis as a falsifiable sentence naming input, system behavior and observable result, so the test can fail clearly instead of drifting into vague confirmation. Use when proof work begins and the claim to be demonstrated is still loose or implied"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [hypothesis, design, rigor]
---

# Weakness Hypothesis Statement

> Write the proof's hypothesis as a falsifiable sentence naming input, system behavior and observable result, so the test can fail clearly instead of drifting into vague confirmation

**Use when:** proof work begins and the claim to be demonstrated is still loose or implied

**Avoid when:** a prior reproduction already fixed the exact inputs and observation

## Procedure

1. State the input you will control: parameter, header, object or sequence you intend to vary.
2. State the system behavior you expect to occur that authorization should prevent.
3. State the observable result that would confirm the expectation in a way a reviewer can check.
4. State the observation that would falsify it, so the test has a real chance of failing.
5. Keep one hypothesis per proof, splitting combined claims into separate testable statements.
6. Date the hypothesis and keep later revisions visible rather than overwriting the original.

## Signals

- The claim reads as an outcome such as the endpoint is insecure with no input or observable named.
- Two independent claims are bundled, so a single result cannot resolve them.
- No falsifier exists, which means any observation could be read as confirmation.
- The hypothesis changed mid-test without a dated revision, muddying what was actually tested.

## Patterns

**1. Hypothesis line**

```text
given=member-a-session when=request-then=order-owned-by-b expect=200-with-b-data falsifier=403-or-404
```

**2. Split note**

```text
was=read-and-write-claim now=read-claim-only reason=one-observable-per-hypothesis
```

**3. Revision**

```text
v1=2026-10-26 v2=2026-10-27 change=input-header-not-body reason=first-falsified note=history-kept
```

## Pitfalls

- Writing a hypothesis that no possible result could refute, which makes the test decorative.
- Bundling claims so a partial result gets reported as full confirmation.
- Rewriting the hypothesis after seeing results, which converts a test into a rationalization.
- Leaving input, behavior or observation implicit, so triage must infer what was tested.

## Done when

- The hypothesis is one falsifiable sentence naming input, expected behavior and observable result.
- A falsifier is written down before execution and results are judged against it.
- Revisions are dated and additive rather than silent overwrites.

## References

- [OWASP - testing guidance for test design](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
