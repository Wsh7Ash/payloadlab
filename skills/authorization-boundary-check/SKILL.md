---
name: authorization-boundary-check
description: "Confirm in writing exactly which assets, actions and data your authorization covers before building any proof, so every test request sits inside a documented permission boundary. Use when starting proof work on a target where scope, rules or permission must be verified first"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [authorization, scope, safety]
---

# Authorization Boundary Check

> Confirm in writing exactly which assets, actions and data your authorization covers before building any proof, so every test request sits inside a documented permission boundary

**Use when:** starting proof work on a target where scope, rules or permission must be verified first

**Avoid when:** a signed engagement letter already names the assets, actions and data you may test

## Procedure

1. Copy the governing scope statement verbatim into the test record so interpretation starts from the actual text.
2. List each asset you intend to touch and mark it explicit, inferred or disputed against that text.
3. Confirm which actions are permitted: sending test requests, creating test data, accessing other test accounts.
4. Note exclusions and voiding conditions such as third-party hosts, active-user data or blackout windows.
5. Send a confirmation question for every disputed item and wait for an answer before testing that item.
6. Version the record so later scope edits show precisely which permission changed and when.

## Signals

- The scope names a platform rather than hosts, leaving every subdomain's status ambiguous.
- Policy language such as similar to or adjacent to silently widens the written asset list.
- A separate safety section contradicts the scope table, which means the narrower reading must govern.
- No contact has answered your confirmation question, yet the test window is already open.

## Patterns

**1. Boundary row**

```text
asset=api.example.com status=explicit action=send-test-requests status=confirmed asset=staging status=disputed
```

**2. Permission line**

```text
may=[scan,create-test-data,read-own-test-records] may-not=[touch-live-user-data] source=policy-2026-10-27
```

**3. Question log**

```text
asked=does-similar-include-staging sent=2026-10-27 reply=pending testing-on-this-item=blocked
```

## Pitfalls

- Starting with the widest reading of scope because it yields more room to test.
- Treating an unanswered confirmation as implicit approval, which removes your documented permission.
- Testing on live user data because the scope text never explicitly said you could not.
- Relying on a remembered scope instead of a versioned record when the program has since edited it.

## Done when

- Every intended asset and action is marked explicit, inferred or disputed with a source citation.
- Disputed items have a sent confirmation and no testing has begun on them.
- The record is versioned so future scope edits diff against a known baseline.

## References

- [ISO 29147 - vulnerability disclosure](https://www.iso.org/standard/72311.html)
- [CISA - coordinated vulnerability disclosure guidance](https://www.cisa.gov/coordinated-vulnerability-disclosure-process)
