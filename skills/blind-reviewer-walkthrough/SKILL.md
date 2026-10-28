---
name: blind-reviewer-walkthrough
description: "Give the finished report to someone who has never seen the test and fix everything they stumble on, because their confusion is the exact confusion triage will feel. Use when a finding is complete and a second reader is available before submission"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [report, quality, writing]
---

# Blind Reviewer Walkthrough

> Give the finished report to someone who has never seen the test and fix everything they stumble on, because their confusion is the exact confusion triage will feel

**Use when:** a finding is complete and a second reader is available before submission

**Avoid when:** you are working alone and no reader is available at all

## Procedure

1. Hand the draft to a reader with no context and ask them to follow it without asking you questions.
2. Have them mark every place they had to guess, re-read or consult something else.
3. Collect their questions verbatim, since each question is a defect in the document, not in them.
4. Fix the document at each mark: add the missing precondition, reorder the buried fact, name the referent.
5. Re-run a second reader if the edits were substantial, because edits can introduce new confusion.
6. Keep the question list, since recurring questions reveal structural weaknesses worth fixing permanently.

## Signals

- Your reader stops to ask what the target asset is, which should be on the first screen.
- They cannot follow the reproduction without you narrating it, which triage cannot do.
- Questions cluster around one section, which marks where the structure fails.
- You explain verbally instead of writing the explanation down, so the document never improves.

## Patterns

**1. Reader mark**

```text
q=which-account-do-i-use-during-step-3 location=repro-steps fix=add-precondition-line
```

**2. Question log**

```text
questions=7 structural=3 factual=4 fixed=7 second-reader-needed=no
```

**3. Recurrence**

```text
theme=impact-unclear across=3-drafts action=rewrite-impact-section-not-sentence
```

## Pitfalls

- Defending the document against questions instead of fixing it at each question mark.
- Answering verbally without editing, so the next reader hits the same wall.
- Using a reader who already knows the test, whose fluency hides the document's gaps.
- Skipping a second pass after substantial edits, which can introduce fresh confusion.

## Done when

- A reader unfamiliar with the test attempted the walkthrough without your narration.
- Every question they raised produced an edit to the document.
- Recurring questions are recorded as structural weaknesses rather than one-off fixes.

## References

- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
- [OWASP - testing guidance for report quality](https://owasp.org/www-project-web-security-testing-guide/)
