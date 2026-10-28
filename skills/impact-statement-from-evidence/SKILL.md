---
name: impact-statement-from-evidence
description: "Derive impact only from what the evidence demonstrates, separating demonstrated capability from plausible extension, so the claim neither undersells nor outruns its support. Use when writing the impact section of a finding from completed evidence"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [report, impact, rigor]
---

# Impact Statement From Evidence

> Derive impact only from what the evidence demonstrates, separating demonstrated capability from plausible extension, so the claim neither undersells nor outruns its support

**Use when:** writing the impact section of a finding from completed evidence

**Avoid when:** impact is prescribed by the program's severity template independently of your evidence

## Procedure

1. State the capability your evidence directly demonstrates, in terms of what an authorized tester achieved.
2. Quantify with observed facts: records seen, objects created, boundary crossed, all counted not estimated.
3. Separate demonstrated impact from plausible extension into two visibly distinct statements.
4. Bound the claim by naming what was not tested and what additional access would still be required.
5. Map the demonstrated part onto the program's severity criteria with one line of reasoning per criterion.
6. Keep the asserted figures with the record so a post-fix re-test can confirm they still hold.

## Signals

- The impact section describes category labels rather than what a victim loses.
- Numbers appear that were extrapolated rather than observed in your own captures.
- Demonstrated and speculative impact are interleaved, so a reviewer cannot separate them.
- Severity is asserted without mapping to the program's published criteria.

## Patterns

**1. Impact line**

```text
demonstrated=cross-tenant-read count=37-records-per-page untested=bulk-export bounded-by=requires-valid-account
```

**2. Separation**

```text
shown=read-one-other-tenant plausible=all-tenants labeling=separate-sentences note=plausible-not-claimed
```

**3. Severity map**

```text
criteria=data-exposure=high criteria=auth-required=low criteria=interaction=none final=high rationale=one-line
```

## Pitfalls

- Inflating with hypotheticals, which lets triage discount the whole report on one overstated figure.
- Framing impact as a category instead of a loss, which invites a default severity assignment.
- Interleaving demonstrated and speculative impact, so neither reads as trustworthy.
- Forgetting the figures asserted, so a post-fix re-test contradicts the original claim.

## Done when

- Demonstrated impact is stated concretely with observed counts, separated visibly from extension.
- The claim is bounded by what was untested and what access it still assumes.
- Severity maps to the program's criteria with a one-line rationale each.

## References

- [FIRST - Common Vulnerability Scoring System](https://www.first.org/cvss/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
