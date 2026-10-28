---
name: non-destructive-test-design
description: "Design proofs that demonstrate capability through reversible, observable effects rather than damage, so evidence is convincing and the system is no worse afterward than before. Use when choosing how to demonstrate a weakness without altering, corrupting or destroying anything"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [safety, design, evidence]
---

# Non Destructive Test Design

> Design proofs that demonstrate capability through reversible, observable effects rather than damage, so evidence is convincing and the system is no worse afterward than before

**Use when:** choosing how to demonstrate a weakness without altering, corrupting or destroying anything

**Avoid when:** the program explicitly requests a specific destructive demonstration in a sandbox

## Procedure

1. Identify what must be shown: unauthorized read, unauthorized write, or control flow you should not hold.
2. For each, choose the least harmful effect that proves it, such as creating one clearly marked object.
3. Prefer read-only demonstration over mutation, and reversible mutation over irreversible change.
4. Design the effect so its presence is obvious and its cleanup is a documented, complete step.
5. Check the demonstration still convinces a skeptic when presented with its evidence chain.
6. Write the cleanup step into the plan before execution, never after the test succeeds.

## Signals

- The planned effect would corrupt or delete data nobody can restore.
- A simpler destructive test is tempting, and the non-destructive version needs more design work.
- The demonstration would be indistinguishable from real activity during later log review.
- Cleanup exists as an intention rather than as a specific, ordered procedure.

## Patterns

**1. Design line**

```text
claim=write-access least-effect=create-1-marked-record reversibility=delete-restores-all cleanup=step-listed
```

**2. Marker note**

```text
object=report-lab-118 marker=lab-do-not-file visible-to=operators cleanup=delete-after-run
```

**3. Choice note**

```text
option=overwrite-real-row rejected=no restore=impossible option=create-marked-row chosen=yes
```

## Pitfalls

- Choosing the fastest demonstration, which is usually the destructive one.
- Leaving cleanup as an afterthought, so a successful test leaves residue behind.
- Making the effect subtle enough to be mistaken for genuine activity in an audit.
- Over-demonstrating: proving write access five times when once is sufficient.

## Done when

- The demonstration proves the claim with the least harmful reversible effect available.
- The marked test object or effect is clearly identifiable as test activity.
- A complete cleanup step is written into the plan before execution.

## References

- [OWASP - testing guidance for safe verification](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
