---
name: test-identity-provisioning
description: "Create the accounts, roles and owned data your proof needs in advance, with each identity's purpose recorded, so the test never borrows a stranger's account or a colleague's data. Use when the proof requires two or more roles, tenants or accounts to demonstrate a boundary crossing"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [setup, test-data, safety]
---

# Test Identity Provisioning

> Create the accounts, roles and owned data your proof needs in advance, with each identity's purpose recorded, so the test never borrows a stranger's account or a colleague's data

**Use when:** the proof requires two or more roles, tenants or accounts to demonstrate a boundary crossing

**Avoid when:** a single pre-provisioned test account already exercises the behavior under test

## Procedure

1. List every identity the proof needs: roles, plan tiers, tenants and ownership relationships.
2. Create each identity fresh, recording its purpose and which step of the proof will use it.
3. Give each identity its own owned objects so ownership boundaries have something real to cross.
4. Label every identity with a marker you can spot later, so cleanup and evidence review stay unambiguous.
5. Verify the identities hold no real personal data and no inherited access from other tests.
6. Store the mapping of identity to purpose with the test record for cleanup and audit.

## Signals

- You are about to reuse an account from an earlier session whose state you no longer know.
- Two test accounts share a team, group or tenant, which may make an intended boundary crossing look valid.
- An identity was created earlier for a different purpose and carries data your current proof does not need.
- No record exists of which identity served which step, so cleanup will guess.

## Patterns

**1. Identity table**

```text
id=test-a-2026 role=member tenant=t1 purpose=actor owns=orders[4471] marker=lab-01
```

**2. Pairing line**

```text
actor=test-a-2026 victim=test-b-2026 shared-team=no shared-tenant=no boundary=cross-tenant
```

**3. Purity note**

```text
real-personal-data=no inherited-access=no created-for=current-proof=yes cleanup-owner=you
```

## Pitfalls

- Reusing an account whose accumulated state makes the observation unreproducible for anyone else.
- Sharing a team between the two identities, then reporting an isolation break the product intends.
- Seeding identities with real user data, which turns a lab setup into a data-handling problem.
- Skipping the identity-to-purpose record, so teardown removes the wrong accounts or keeps the wrong ones.

## Done when

- Every identity needed by the proof exists with purpose, owned objects and a visible marker recorded.
- No identity holds real personal data or unintended inherited access.
- The identity-to-purpose mapping is stored with the test record for teardown.

## References

- [OWASP - testing guidance for test data](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
