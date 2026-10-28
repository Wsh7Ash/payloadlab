---
name: request-sequence-ordering
description: "Order the proof's requests so each step's state is established before the next depends on it, because out-of-order execution produces failures that look like negative results. Use when the proof needs several requests whose later ones depend on earlier state"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [deliver, sequence, rigor]
---

# Request Sequence Ordering

> Order the proof's requests so each step's state is established before the next depends on it, because out-of-order execution produces failures that look like negative results

**Use when:** the proof needs several requests whose later ones depend on earlier state

**Avoid when:** a single self-contained request makes the demonstration

## Procedure

1. Write the sequence as an ordered list where each step names the state it establishes.
2. Mark dependencies between steps so the required ordering is explicit rather than implied.
3. Execute in the written order and stop to diagnose when a step fails, rather than continuing blind.
4. Verify each precondition produced by a prior step before relying on it downstream.
5. Re-run the sequence from clean state if any step was retried, since retries can reorder effects.
6. Record the executed order with results, so a failed run can be replayed step for step.

## Signals

- A later request failed because an earlier one had not yet completed its side effect.
- Steps were parallelized for speed, which destroyed the state ordering the proof depends on.
- A step was retried and the retry raced the next step in the sequence.
- The executed order differs from the planned order with no note explaining the deviation.

## Patterns

**1. Sequence**

```text
1=create-object establishes=owned-row 2=second-user-acts requires=owned-row 3=observe requires=act-2
```

**2. Failure note**

```text
step=2 failed cause=step-1-write-not-yet-visible action=insert-wait-then-retry logged=yes
```

**3. Retry rule**

```text
retried=step-1 consequence=re-run-from-clean-start reason=race-effect-state-replay
```

## Pitfalls

- Continuing past a failed dependency step, which makes every later result meaningless.
- Parallelizing steps whose ordering carries meaning.
- Retrying mid-sequence and never re-running from the start, leaving state inconsistent.
- Keeping the executed order only in memory, so failures cannot be replayed.

## Done when

- The sequence is written with each step's established state and its dependencies marked.
- Execution followed the written order with failures diagnosed at the step they occurred.
- The executed order and outcomes are recorded with the evidence.

## References

- [OWASP - testing guidance for test sequences](https://owasp.org/www-project-web-security-testing-guide/)
- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
