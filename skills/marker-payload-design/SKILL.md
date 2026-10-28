---
name: marker-payload-design
description: "Design a unique recognizable marker for your proof so the observation can never be confused with coincidental content the system already contained. Use when the proof depends on recognizing whether your input appeared somewhere it should not"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [craft, markers, evidence]
---

# Marker Payload Design

> Design a unique recognizable marker for your proof so the observation can never be confused with coincidental content the system already contained

**Use when:** the proof depends on recognizing whether your input appeared somewhere it should not

**Avoid when:** the observation is a status code or structural change with no content matching involved

## Procedure

1. Compose a marker with a unique token you chose, such as a dated prefix plus a random suffix.
2. Keep the marker inside the constraints of the destination context: length, allowed characters and format.
3. Make the marker impossible or vanishingly unlikely to exist in real content before your test.
4. Ensure the marker survives the transformation path you documented during context classification.
5. Record the exact marker string with the test so later searches can find every occurrence.
6. Prefer markers that are visibly artificial, so accidental matches read as test data instantly.

## Signals

- The marker you picked is a common word that could appear in genuine content by chance.
- The marker is longer than a field's limit, so it would be truncated before reaching the sink.
- Characters in the marker are altered by encoding, so the arriving value no longer matches what you search for.
- No record of the exact marker exists, so later occurrence checks rely on memory.

## Patterns

**1. Marker line**

```text
marker=lab-20261027-7f3a9d context=html-attribute length=19 allowed=alphanum-and-dash collision=improbable
```

**2. Survival check**

```text
sent=lab-20261027-7f3a9d arrived=lab-20261027-7f3a9d transform=entity-encode not-hit=yes match-exact
```

**3. Occurrence search**

```text
marker=lab-20261027-7f3a9d searched=responses[14] hits=1 first-hit=response-9 note=recorded-where
```

## Pitfalls

- Choosing a generic marker such as test123 that real content may already contain, faking a hit.
- Ignoring field length limits, so truncation makes the marker unusable for exact matching.
- Not verifying the marker survives the transformation path, then failing to find a real occurrence.
- Letting the marker appear in unrelated requests, so a later hit cannot be attributed to a specific test.

## Done when

- The marker is unique, context-legal and recorded exactly with the test record.
- A survival check confirms the marker arrives unchanged or in a predicted transformed form.
- The search procedure for finding the marker in responses is defined and repeatable.

## References

- [OWASP - testing guidance for verifiable evidence](https://owasp.org/www-project-web-security-testing-guide/)
- [CWE - weakness catalog](https://cwe.mitre.org/)
