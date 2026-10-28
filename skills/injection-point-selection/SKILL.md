---
name: injection-point-selection
description: "Select the exact parameter, header or field where the proof enters, naming why that point reaches the behavior under test, so evidence maps to a specific entry the fix can address. Use when multiple candidate entry points exist for the same downstream behavior"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [deliver, craft, recon]
---

# Injection Point Selection

> Select the exact parameter, header or field where the proof enters, naming why that point reaches the behavior under test, so evidence maps to a specific entry the fix can address

**Use when:** multiple candidate entry points exist for the same downstream behavior

**Avoid when:** there is exactly one input and its path is documented

## Procedure

1. List candidate entry points that plausibly reach the component named in your hypothesis.
2. Rank them by how directly they reach it, preferring points with the shortest unobstructed path.
3. Check each candidate for transformations that would alter your proof before arrival.
4. Pick one primary point and name a backup, since a single point can be blocked or filtered.
5. Record the selection with the reason, so the report ties the observation to a concrete entry.
6. Re-select deliberately if the primary point fails, rather than silently spraying every candidate.

## Signals

- Several parameters reach the same handler and you cannot say which one your evidence used.
- The chosen point transforms input in a way your proof did not account for.
- Every candidate was tried in sequence, which reads as spraying rather than as a deliberate test.
- No backup point was identified, so one filter defeats the entire proof.

## Patterns

**1. Select row**

```text
point=param-search reach=direct transform=url-decode primary=yes reason=shortest-path backup=header-x
```

**2. Rejected point**

```text
point=cookie rejected=never-reaches-handler evidence=server-ignores-cookie note=not-tested-elsewhere
```

**3. Switch point**

```text
primary=param-search outcome=filtered action=switch-to-backup logged=2026-10-27 reason=one-substitution
```

## Pitfalls

- Testing every point at once, which obscures which entry actually carried the proof.
- Choosing a point that transforms your input without accounting for the transformation.
- Reporting an observation without naming the entry point, leaving the fix untargetable.
- Switching points repeatedly without logging, so the evidence chain fragments.

## Done when

- A primary entry point is chosen with its reasoning and a backup identified.
- Transformations at the chosen point are accounted for in the proof.
- The report ties the observation to the specific entry point used.

## References

- [OWASP - testing guidance for injection points](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
