---
name: benign-proof-technique-selection
description: "Choose the least invasive technique that still demonstrates the claim, preferring visible no-op effects over state changes, so the proof convinces without costing anyone cleanup. Use when several demonstration approaches could prove the same weakness"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [craft, safety, design]
---

# Benign Proof Technique Selection

> Choose the least invasive technique that still demonstrates the claim, preferring visible no-op effects over state changes, so the proof convinces without costing anyone cleanup

**Use when:** several demonstration approaches could prove the same weakness

**Avoid when:** the program's report template mandates a specific demonstration form

## Procedure

1. List the demonstration options available for the claim, from read-only to state-changing.
2. Rank them by invasiveness, putting observation first, reversible writes second, side effects last.
3. Select the lowest-ranked option that still satisfies your declared success criteria.
4. Verify the chosen technique still produces evidence strong enough for a skeptical reviewer.
5. Document why higher-invasiveness options were rejected, so the choice reads as deliberate.
6. Re-check the choice if the first technique fails to demonstrate, rather than escalating automatically.

## Signals

- The cheapest demonstration would notify real users or leave state an operator must clean up.
- You are escalating invasiveness without recording why the gentler technique was insufficient.
- A read-only demonstration exists but was skipped because the write-based one felt more convincing.
- The chosen technique leaves artifacts indistinguishable from genuine activity in log review.

## Patterns

**1. Rank list**

```text
1=read-only-observe 2=create-marked-object 3=modify-marked-object 4=side-effecting chosen=1 suffices=yes
```

**2. Reject note**

```text
option=send-notification rejected=would-reach-real-users option=overwrite-row rejected=irreversible
```

**3. Escalation**

```text
first=observe-insufficient reason=no-visible-difference next=create-one-marked-record logged=yes
```

## Pitfalls

- Defaulting to the most dramatic demonstration when a quieter one proves the same point.
- Escalating invasiveness without documenting the insufficiency of the gentler attempt.
- Picking a technique that produces evidence no reviewer can verify independently.
- Leaving artifacts that resemble real activity, which damages trust during later audit review.

## Done when

- The chosen technique is the least invasive option that satisfies the declared success criteria.
- Rejected higher-invasiveness options are recorded with reasons.
- The technique produces evidence a reviewer can verify without relying on your account alone.

## References

- [OWASP - testing guidance for safe proof](https://owasp.org/www-project-web-security-testing-guide/)
- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
