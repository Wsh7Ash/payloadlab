---
name: reviewer-legible-payload-authoring
description: "Author proofs whose every element a reviewer can explain, so the submission reads as an engineering demonstration rather than an opaque recipe copied from somewhere. Use when the proof works but its individual pieces have no stated purpose"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [craft, writing, evidence]
---

# Reviewer Legible Payload Authoring

> Author proofs whose every element a reviewer can explain, so the submission reads as an engineering demonstration rather than an opaque recipe copied from somewhere

**Use when:** the proof works but its individual pieces have no stated purpose

**Avoid when:** the program requests raw requests without explanation

## Procedure

1. Annotate each element of the proof with the job it performs in the demonstration.
2. Replace unexplained magic values with ones whose purpose is evident from the string itself.
3. Split compound elements so each line carries exactly one responsibility.
4. State the intended effect of each annotated element next to the observed effect.
5. Cut elements that serve no purpose in the demonstration, which only add review noise.
6. Read the annotated proof as a reviewer would and mark anything you cannot explain in seconds.

## Signals

- Elements exist that nobody can explain, which reviewers will read as copied material.
- The proof contains values that look authoritative but have no bearing on the claim.
- One line combines three behaviors, so a failure in any one is undiagnosable.
- You cannot narrate the proof aloud without hesitating, which a reviewer will notice immediately.

## Patterns

**1. Annotate**

```text
element=marker purpose=observable-proof element=close-attribute purpose=end-surrounding-syntax effect=structured-parse
```

**2. Split line**

```text
was=send-and-read-hateoas-link now=1=send-now=parse-response reason=one-behavior-per-line
```

**3. Cut record**

```text
removed=extra-header reason=no-bearing-on-claim removed=dead-field reason=server-ignores-it
```

## Pitfalls

- Shipping a proof full of cargo-cult values that distract from the actual mechanism.
- Annotating after submission, so reviewers meet the opaque version first.
- Splitting lines until the sequence is unreadable, trading one failure mode for another.
- Keeping elements that demonstrate nothing, which invites questions you do not want to answer.

## Done when

- Every element carries a stated purpose a reviewer can check against its observed effect.
- No unexplained magic values remain in the proof.
- Elements with no bearing on the claim have been removed.

## References

- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
- [OWASP - testing guidance for proof quality](https://owasp.org/www-project-web-security-testing-guide/)
