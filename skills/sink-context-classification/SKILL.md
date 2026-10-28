---
name: sink-context-classification
description: "Classify where your input lands and how the system interprets it, because the context determines what a valid proof must contain and what an invalid one merely appears to contain. Use when input reaches a rendering, parsing, query, path or template context that could misinterpret it"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [context, hypothesis, encoding]
---

# Sink Context Classification

> Classify where your input lands and how the system interprets it, because the context determines what a valid proof must contain and what an invalid one merely appears to contain

**Use when:** input reaches a rendering, parsing, query, path or template context that could misinterpret it

**Avoid when:** input is echoed back through a single well-understood encoding with no interpretation

## Procedure

1. Identify the destination context of the input: markup, script, attribute, query, path, template or data field.
2. Determine how the system transforms input on the way in: decoding, escaping, normalization or truncation.
3. Write down the context and transformation as facts, separating what you observed from what you inferred.
4. Check whether the same value passes through multiple contexts in sequence, since each changes the requirement.
5. Confirm classification with an observation rather than an assumption about the framework in use.
6. Record the classification next to the hypothesis, since it governs what the proof must demonstrate.

## Signals

- Input passes through two contexts, such as a query parsed then a value rendered, and only one was considered.
- You classified the context by framework reputation instead of by observed transformation.
- Truncation or normalization alters the value between what you sent and what arrives.
- The proof's payload was built for one context while the system interprets another.

## Patterns

**1. Context line**

```text
input=search-param destination=html-attribute transform=entity-encode-on-render verified=by-echo-test
```

**2. Chain note**

```text
ctx1=query-string transform=url-decode ctx2=attribute-value transform=entity-encode implication=encode-for-final-ctx
```

**3. Observed row**

```text
sent=marker with-char=< arrived=marker-with-char=&lt; classification=attribute-context-confirmed
```

## Pitfalls

- Guessing the context from the framework instead of observing what actually happens to the value.
- Classifying only the final context when the input passes through earlier ones that also transform it.
- Ignoring truncation, which silently changes payload length assumptions.
- Treating classification as proven when only inferred, then building the whole proof on it.

## Done when

- The destination context and its transformations are recorded as observations, not assumptions.
- Multi-context paths are documented with each transformation applied.
- Classification is confirmed by a probe, not by framework reputation.

## References

- [OWASP - cross-site scripting prevention cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [CWE - weakness catalog for improper encoding](https://cwe.mitre.org/)
