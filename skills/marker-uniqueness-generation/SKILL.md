---
name: marker-uniqueness-generation
description: "Generate markers with enough entropy and a dating convention that collisions with real content are practically impossible and every marker can be traced to its test. Use when multiple proofs run over time and markers must not collide with each other or with real content"
pack: payloadlab
version: 1.0.0
category: defensive-security
tags: [markers, craft, records]
---

# Marker Uniqueness Generation

> Generate markers with enough entropy and a dating convention that collisions with real content are practically impossible and every marker can be traced to its test

**Use when:** multiple proofs run over time and markers must not collide with each other or with real content

**Avoid when:** a single throwaway test runs once and its marker will never be searched again

## Procedure

1. Include a date and a random component in every marker so it is both unique and locatable in time.
2. Draw the random component from a real source with enough bits that collision is not a concern.
3. Add a short test identifier so a marker maps back to a specific proof without a lookup table.
4. Check the composed marker against recent captured content to confirm no pre-existing occurrence.
5. Register the marker in the test record before use, so it exists on record before it appears anywhere.
6. Keep one registry across tests so repeated or overlapping markers are detected before deployment.

## Signals

- Markers are hand-written, which makes repeated or colliding values easy to produce by accident.
- A marker has no date component, so its origin cannot be determined from the string alone.
- The same marker was used in two tests, so a later occurrence cannot be attributed to either.
- No registry exists, so uniqueness is checked by memory rather than by search.

## Patterns

**1. Compose marker**

```text
marker=lab-20261027-poc118-7f3a9d bits-of-random=24 traceable-to=poc-118 registry=checked
```

**2. Pre-check**

```text
searched=captured-content hits=0 verdict=clean-to-deploy note=ran-before-first-request
```

**3. Registry row**

```text
marker=lab-20261027-poc118-7f3a9d test=poc-118 first-used=09:14 status=active cleanup=due
```

## Pitfalls

- Reusing a marker across tests, which destroys attribution when an occurrence finally shows up.
- Writing markers by hand without a registry, so collisions are discovered in the evidence.
- Skipping the pre-check, then finding the marker already existed in real content.
- Omitting the test identifier, forcing a lookup table to connect a marker to its proof.

## Done when

- Every marker combines date, random entropy and a test identifier.
- Uniqueness is verified against captured content before first use.
- A registry maps each marker to its test and its cleanup status.

## References

- [NIST - guidance on random values](https://csrc.nist.gov/pubs/sp/800/90/a/final)
- [CWE - weakness catalog](https://cwe.mitre.org/)
