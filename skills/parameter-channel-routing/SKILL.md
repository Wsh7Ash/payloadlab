---
name: parameter-channel-routing
description: "Know which channel carries your proof into the application, query string, body, header, cookie or path, since the channel determines both the transformation applied and the fix required. Use when the same logical value can travel through several channels to reach one handler"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [deliver, recon, context]
---

# Parameter Channel Routing

> Know which channel carries your proof into the application, query string, body, header, cookie or path, since the channel determines both the transformation applied and the fix required

**Use when:** the same logical value can travel through several channels to reach one handler

**Avoid when:** the channel is fixed and documented by the interface under test

## Procedure

1. Identify the channel the real application uses for this value in normal operation.
2. Confirm your proof travels the same channel, since a different channel may take a different path.
3. Check whether each candidate channel applies its own parsing, length limit or normalization.
4. Note which channel your selected injection point uses and what that implies for transformation.
5. Test one channel at a time rather than mirroring the value across all of them at once.
6. Record channel results separately, since identical values can behave differently by channel.

## Signals

- The same value behaves differently in body and header, which means the channels are not equivalent.
- Your proof went through a channel the application never uses for that value in production.
- Channels were mirrored simultaneously, so no channel's result can be attributed cleanly.
- A channel applies its own normalization you did not account for in the proof.

## Patterns

**1. Channel table**

```text
channel=query transform=url-decode limit=256-reached=no channel=header transform=none limit=8k
```

**2. Route note**

```text
value=auth-token app-channel=header test-channel=query implication=different-path-not-equivalent
```

**3. Result split**

```text
body-result=marker-arrived header-result=marker-filtered note=per-channel-results-kept-separate
```

## Pitfalls

- Mirroring a value across every channel at once, which produces results nobody can attribute.
- Assuming channels are equivalent when they differ in parsing, limits or routing.
- Testing a channel production never uses, so the evidence does not map to real traffic.
- Ignoring channel-specific normalization, which alters your proof before arrival.

## Done when

- The production channel for the value is identified and the proof uses it.
- Channel-specific transformations and limits are documented.
- Results are recorded per channel rather than merged.

## References

- [OWASP - testing guidance for parameter handling](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
