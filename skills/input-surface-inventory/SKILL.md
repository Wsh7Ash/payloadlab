---
name: input-surface-inventory
description: "Enumerate every channel through which your input can reach the system before proving one of them, so the proof names its exact entry point and acknowledges the ones it did not test. Use when the target accepts input through several channels and the proof must name its own"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [inventory, hypothesis, recon]
---

# Input Surface Inventory

> Enumerate every channel through which your input can reach the system before proving one of them, so the proof names its exact entry point and acknowledges the ones it did not test

**Use when:** the target accepts input through several channels and the proof must name its own

**Avoid when:** a single documented input path exists for the behavior under test

## Procedure

1. List every channel: query, body fields, headers, cookies, path segments, files and asynchronous jobs.
2. For each, note whether it reaches the component your hypothesis concerns.
3. Mark which channels the proof will exercise and which it deliberately leaves untested.
4. Check for channels that transform input before use, since transformation changes what the proof should send.
5. Record the inventory with the hypothesis so coverage claims stay honest.
6. Update the list when a channel appears during testing rather than assuming the list was complete.

## Signals

- The proof targets a query parameter while an equivalent body parameter reaches the same code path.
- A channel normalizes or decodes input, which means your test value arrives changed.
- Channels exist that nobody enumerated, discovered only when a reviewer asks about them.
- The report claims the endpoint is vulnerable without naming which channel carried the input.

## Patterns

**1. Surface row**

```text
channel=query reachable=yes tested=yes channel=header reachable=yes tested=no reason=out-of-scope-this-round
```

**2. Transform note**

```text
channel=body transform=url-decode-on-arrival implication=test-value-must-arrive-encoded
```

**3. Coverage**

```text
tested=1-of-4 claim-limited-to=tested-channel disclosed-untested=[header,cookie,path]
```

## Pitfalls

- Proving one channel while implying the claim covers all of them.
- Ignoring input transformation, so the value you sent is not the value that arrived.
- Never recording which channels went untested, which leaves coverage overstated.
- Treating the inventory as fixed when channels appear mid-test.

## Done when

- Every known input channel is listed with reachability and test status.
- The proof names the exact channel it exercises and discloses the untested ones.
- Input transformations relevant to the test are documented.

## References

- [OWASP - testing guidance for input surfaces](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog for input validation](https://cwe.mitre.org/)
