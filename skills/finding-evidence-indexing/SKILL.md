---
name: finding-evidence-indexing
description: "Build an index mapping every claim in the finding to the artifact that proves it, so a reviewer can audit the report without hunting through attachments. Use when the finding carries multiple claims and multiple pieces of evidence"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [report, evidence, records]
---

# Finding Evidence Indexing

> Build an index mapping every claim in the finding to the artifact that proves it, so a reviewer can audit the report without hunting through attachments

**Use when:** the finding carries multiple claims and multiple pieces of evidence

**Avoid when:** the report is two sentences with one attached capture

## Procedure

1. List every distinct claim the report makes, from the headline down to incidental assertions.
2. Name the single artifact that proves each claim, preferring one strong artifact over several weak ones.
3. Mark any claim with no artifact, and either attach proof or cut the claim from the report.
4. Order the index to match the report's structure so both can be read side by side.
5. Verify each indexed artifact exists, is legible and carries no unredacted secret.
6. Include the index in the submission, since an index left out is an index nobody uses.

## Signals

- Claims outnumber the artifacts that support them, which means at least one claim rests on assertion.
- Evidence was attached in capture order rather than claim order, so the two cannot be read together.
- An indexed artifact does not exist or cannot be opened by the reviewer.
- The index lives outside the submission, so triage never sees the mapping you prepared.

## Patterns

**1. Index row**

```text
claim=cross-tenant-read artifact=evidence-01-diff.txt claim=scale artifact=evidence-02-count-note.txt
```

**2. Gap record**

```text
claim=rate-limit-absent artifact=none action=test-it-or-cut-the-claim status=claim-cut
```

**3. Order match**

```text
report-sections=1-6 index-order=same-as-sections reviewer-can-walk-both=yes
```

## Pitfalls

- Letting a claim ship with no artifact, which a reviewer will eventually notice.
- Ordering artifacts by capture time instead of by claim, so the audit requires jumping around.
- Indexing an artifact that is illegible at normal zoom, which is effectively missing.
- Preparing the index and then omitting it from the submission.

## Done when

- Every claim in the report maps to one proving artifact, or the claim has been cut.
- The index follows the report's structure and is included in the submission.
- All indexed artifacts exist, are legible and carry no unredacted secrets.

## References

- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
- [NIST - audit and accountability guidance](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
