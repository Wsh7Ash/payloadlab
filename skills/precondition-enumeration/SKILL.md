---
name: precondition-enumeration
description: "List every state, role, flag and prior action your proof depends on, so reproduction works on the first attempt and triage never has to guess what setup the test assumed. Use when the proof requires a specific starting state to trigger"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [setup, hypothesis, reproduction]
---

# Precondition Enumeration

> List every state, role, flag and prior action your proof depends on, so reproduction works on the first attempt and triage never has to guess what setup the test assumed

**Use when:** the proof requires a specific starting state to trigger

**Avoid when:** the behavior occurs on a default install with no setup beyond an account

## Procedure

1. List every precondition: role, plan tier, feature flag, prior action, data rows and account age.
2. Order them so the chain executes top to bottom without improvisation or hidden knowledge.
3. Mark each as default, product-obtainable or requiring privileged access to establish.
4. State time dependence: how long setup takes and how long the precondition remains true.
5. Follow the chain literally from a clean environment and fix every ambiguity you hit.
6. Attach the ordered chain to the record, separate from the trigger steps themselves.

## Signals

- The proof assumes two roles in different tenants without stating how that state was created.
- A feature flag must be enabled and the method of enabling it was never recorded.
- The trigger requires accumulated data, so anyone reproducing today cannot match your conditions.
- Triage's first reply is a request for the missing setup, which this chain would have supplied.

## Patterns

**1. Chain line**

```text
1=create-tenant-a 2=create-tenant-b 3=b-creates-order 4=flag-on 5=a-attempts-read expect=denied
```

**2. Flag note**

```text
flag=new-flow default=off how-enabled=admin-console persists=until-redeploy note=state-this
```

**3. Time dep**

```text
precondition=account-age>30d implication=cannot-repro-today mitigation=seed-or-wait note=declare-it
```

## Pitfalls

- Describing setup as narrative prose, forcing the reader to re-derive the order.
- Assuming a precondition is default when your own earlier testing enabled it.
- Omitting time-dependent state, which makes the proof appear non-reproducible to everyone else.
- Mixing prerequisites into trigger steps so neither section can be followed alone.

## Done when

- Preconditions are listed in executable order with their source classified.
- Time dependence and persistence are stated for each.
- The chain has been followed literally from a clean state with ambiguities fixed.

## References

- [OWASP - testing guidance for test cases](https://owasp.org/www-project-web-security-testing-guide/)
- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
