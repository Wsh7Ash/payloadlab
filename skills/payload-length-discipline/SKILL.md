---
name: payload-length-discipline
description: "Account for length limits, truncation and field sizing along the whole path, so a proof never fails silently because the value was cut before it reached where you were watching. Use when input passes through fields, headers, storage columns or filters with size constraints"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [craft, constraints, rigor]
---

# Payload Length Discipline

> Account for length limits, truncation and field sizing along the whole path, so a proof never fails silently because the value was cut before it reached where you were watching

**Use when:** input passes through fields, headers, storage columns or filters with size constraints

**Avoid when:** the path documents no limits and your values are trivially short

## Procedure

1. Find documented length limits for every field, header and storage column on the input's path.
2. Estimate the effective limit empirically by sending a graduated probe and observing where it cuts.
3. Compare your proof's length against the effective limit with margin, not at the boundary.
4. If truncation occurs, decide deliberately whether to shorten the proof or to prove the truncation itself.
5. Record where the cut happened, since silent truncation can be its own observation worth reporting.
6. Re-check limits when a value arrives shortened after an environment or configuration change.

## Signals

- The value arrives shorter than sent, which silently breaks exact marker matching.
- The proof sits within a few characters of a documented limit with no margin for encoding expansion.
- Truncation cuts your closing delimiters, leaving unbalanced structure in the destination.
- Limits differ between environments, so a proof that worked in one place fails in another.

## Patterns

**1. Limit row**

```text
field=search documented=256 measured=250 proof-length=89 margin=plenty status=fit
```

**2. Truncation**

```text
sent=120-chars arrived=80-chars cut-at=80 encoding-expanded=yes action=shorten-or-prove-truncation
```

**3. Boundary note**

```text
proof=248 limit=250 margin=2 verdict=too-close action=shorten-before-executing
```

## Pitfalls

- Discovering the limit when your marker stops matching, then misreading it as a negative result.
- Building at exactly the documented boundary, where encoding expansion pushes the value over.
- Ignoring that truncation can remove your structural closers, changing what the destination parses.
- Treating limits as universal when they vary by field, environment and configuration.

## Done when

- Effective limits are measured or documented for every field on the path.
- The proof fits with margin, or truncation is deliberately demonstrated and recorded.
- Any truncation point is documented with where the cut occurred.

## References

- [OWASP - input validation cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [CWE - weakness catalog for buffer limits](https://cwe.mitre.org/)
