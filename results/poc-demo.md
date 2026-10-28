# PoC runbook - Reflected input observed in an attribute context
Context: html-attribute reflected search parameter on a member-only page   Skills matched: 38 of 50   Plan steps: 24

Thin coverage (no matched skill in these phases): observe, report

## scope

authorization-boundary-check  (match 1)
  Confirm in writing exactly which assets, actions and data your authorization covers before building any proof, so every test request sits inside a documented permission boundary
   1. Copy the governing scope statement verbatim into the test record so interpretation starts from the actual text.
   2. List each asset you intend to touch and mark it explicit, inferred or disputed against that text.
   3. Confirm which actions are permitted: sending test requests, creating test data, accessing other test accounts.
   4. Note exclusions and voiding conditions such as third-party hosts, active-user data or blackout windows.
   5. Send a confirmation question for every disputed item and wait for an answer before testing that item.
   6. Version the record so later scope edits show precisely which permission changed and when.

blast-radius-budget  (match 1)
  Declare the maximum effect your proof is allowed to produce before you build it, so scale, writes and notifications stay inside a budget you chose rather than one the test discovered
   1. Enumerate every side effect the proof could produce: writes, emails, queue jobs, quota use or third-party calls.
   2. Assign each effect a hard ceiling: records touched, messages sent, requests issued, duration of load.
   3. Choose ceilings that prove the claim at minimum scale, since one successful instance is usually enough.
   4. Write the budget into the test record before running anything, so overrun is measurable rather than vague.
   5. Monitor consumption during the test and stop at the ceiling even if the claim is not yet fully proven.
   6. Record actual consumption against the budget so the next test starts from measured reality.

environment-choice-staging-or-prod  (match 1)
  Decide deliberately whether the proof runs against staging, a local build or production, and record why, so the choice is justified by evidence instead of grabbed by default
   1. List candidate environments: local build, staging, sandbox, shared test tenant and production.
   2. Check each for behavioral parity with production, since a stale staging build invalidates the proof.
   3. Weigh risk: production proves the real thing but carries real blast radius, staging may not reproduce.
   4. Confirm authorization covers the environment you choose, since permission rarely spans all of them.
   5. Record the choice with its reasoning and the parity evidence that justified it.
   6. Fall back deliberately if staging fails to reproduce, rather than drifting silently into production.

non-destructive-test-design  (match 1)
  Design proofs that demonstrate capability through reversible, observable effects rather than damage, so evidence is convincing and the system is no worse afterward than before
   1. Identify what must be shown: unauthorized read, unauthorized write, or control flow you should not hold.
   2. For each, choose the least harmful effect that proves it, such as creating one clearly marked object.
   3. Prefer read-only demonstration over mutation, and reversible mutation over irreversible change.
   4. Design the effect so its presence is obvious and its cleanup is a documented, complete step.
   5. Check the demonstration still convinces a skeptic when presented with its evidence chain.
   6. Write the cleanup step into the plan before execution, never after the test succeeds.

scope-record-keeping  (match 1)
  Keep one durable record linking permission, environment, identities and budget for each test, so any later question about what you were allowed to do has a single authoritative answer
   1. Open one record per test containing permission source, environment choice, identities and blast budget.
   2. Append decisions as they are made with dates, rather than reconstructing them afterward from memory.
   3. Attach the evidence for each decision: scope excerpt, confirmation reply, parity check, budget.
   4. Keep the record versioned so a scope change during the test shows as a visible edit.
   5. Store the record with the eventual finding so the report can cite its own authorization basis.
   6. Review the record at close-out to confirm nothing tested exceeded what the record authorized.

## hypothesis

sink-context-classification  (match 3)
  Classify where your input lands and how the system interprets it, because the context determines what a valid proof must contain and what an invalid one merely appears to contain
   1. Identify the destination context of the input: markup, script, attribute, query, path, template or data field.
   2. Determine how the system transforms input on the way in: decoding, escaping, normalization or truncation.
   3. Write down the context and transformation as facts, separating what you observed from what you inferred.
   4. Check whether the same value passes through multiple contexts in sequence, since each changes the requirement.
   5. Confirm classification with an observation rather than an assumption about the framework in use.
   6. Record the classification next to the hypothesis, since it governs what the proof must demonstrate.

variable-isolation-design  (match 2)
  Plan the proof so exactly one variable changes between control and test, making the difference attributable instead of leaving reviewers to guess which of several changes caused it
   1. Identify every factor that could plausibly change the outcome in this test.
   2. Choose the one factor your hypothesis concerns and fix everything else to identical values.
   3. Run a control first: identical conditions with the factor in its normal state.
   4. Change only the chosen factor and run the test, keeping captures from both runs.
   5. If the result differs, attribute it to the single changed factor and say so explicitly.
   6. If the result does not differ, vary one additional factor deliberately in a separate run rather than a combined one.

weakness-hypothesis-statement  (match 2)
  Write the proof's hypothesis as a falsifiable sentence naming input, system behavior and observable result, so the test can fail clearly instead of drifting into vague confirmation
   1. State the input you will control: parameter, header, object or sequence you intend to vary.
   2. State the system behavior you expect to occur that authorization should prevent.
   3. State the observable result that would confirm the expectation in a way a reviewer can check.
   4. State the observation that would falsify it, so the test has a real chance of failing.
   5. Keep one hypothesis per proof, splitting combined claims into separate testable statements.
   6. Date the hypothesis and keep later revisions visible rather than overwriting the original.

expected-behavior-baseline  (match 1)
  Establish what the system should do under normal rules before testing, so the eventual observation is measured against a documented expectation instead of an intuition
   1. Find the authoritative statement of correct behavior: documentation, spec, policy or contract.
   2. Confirm the documented rule against a live observation where possible, since docs drift too.
   3. Capture the correct-case response under conditions identical to the planned test.
   4. Record status, relevant body fields and headers so later comparison is concrete.
   5. Note any variation the system legitimately produces, such as timestamps or identifiers.
   6. Store the baseline with the test record so the comparison survives independent review.

input-surface-inventory  (match 1)
  Enumerate every channel through which your input can reach the system before proving one of them, so the proof names its exact entry point and acknowledges the ones it did not test
   1. List every channel: query, body fields, headers, cookies, path segments, files and asynchronous jobs.
   2. For each, note whether it reaches the component your hypothesis concerns.
   3. Mark which channels the proof will exercise and which it deliberately leaves untested.
   4. Check for channels that transform input before use, since transformation changes what the proof should send.
   5. Record the inventory with the hypothesis so coverage claims stay honest.
   6. Update the list when a channel appears during testing rather than assuming the list was complete.

precondition-enumeration  (match 1)
  List every state, role, flag and prior action your proof depends on, so reproduction works on the first attempt and triage never has to guess what setup the test assumed
   1. List every precondition: role, plan tier, feature flag, prior action, data rows and account age.
   2. Order them so the chain executes top to bottom without improvisation or hidden knowledge.
   3. Mark each as default, product-obtainable or requiring privileged access to establish.
   4. State time dependence: how long setup takes and how long the precondition remains true.
   5. Follow the chain literally from a clean environment and fix every ambiguity you hit.
   6. Attach the ordered chain to the record, separate from the trigger steps themselves.

rival-explanation-elimination  (match 1)
  List the innocent explanations for your observation and test each one, so the finding rests on eliminating alternatives rather than on the first story that fit
   1. Write down every plausible alternative explanation for the observation, including boring ones.
   2. For each rival, name a test that would distinguish it from your hypothesis.
   3. Run the cheapest distinguishing tests first, since one may resolve the question immediately.
   4. Record which rivals were eliminated with evidence and which remain standing.
   5. State remaining rivals in the report if any survive, which strengthens rather than weakens it.
   6. Revisit survivors if later evidence changes, since a leftover rival can invalidate the whole claim.

## craft

context-delimiter-selection  (match 3)
  Choose the delimiters that terminate your input within its destination context so the proof ends where you intend instead of being consumed by surrounding syntax
   1. Identify the surrounding syntax at the destination: which characters open and close the surrounding construct.
   2. Determine how many delimiter levels must be closed, since nested structures need matching closers.
   3. Construct your input so it closes the surrounding construct cleanly before the demonstrative part.
   4. Confirm the closing sequence survives the encoding layers you mapped earlier.
   5. Verify by capture that the system parsed your structure rather than swallowing it as text.
   6. Record the delimiter reasoning with the proof so a reviewer can see why those characters were chosen.

marker-payload-design  (match 3)
  Design a unique recognizable marker for your proof so the observation can never be confused with coincidental content the system already contained
   1. Compose a marker with a unique token you chose, such as a dated prefix plus a random suffix.
   2. Keep the marker inside the constraints of the destination context: length, allowed characters and format.
   3. Make the marker impossible or vanishingly unlikely to exist in real content before your test.
   4. Ensure the marker survives the transformation path you documented during context classification.
   5. Record the exact marker string with the test so later searches can find every occurrence.
   6. Prefer markers that are visibly artificial, so accidental matches read as test data instantly.

payload-length-discipline  (match 3)
  Account for length limits, truncation and field sizing along the whole path, so a proof never fails silently because the value was cut before it reached where you were watching
   1. Find documented length limits for every field, header and storage column on the input's path.
   2. Estimate the effective limit empirically by sending a graduated probe and observing where it cuts.
   3. Compare your proof's length against the effective limit with margin, not at the boundary.
   4. If truncation occurs, decide deliberately whether to shorten the proof or to prove the truncation itself.
   5. Record where the cut happened, since silent truncation can be its own observation worth reporting.
   6. Re-check limits when a value arrives shortened after an environment or configuration change.

benign-proof-technique-selection  (match 2)
  Choose the least invasive technique that still demonstrates the claim, preferring visible no-op effects over state changes, so the proof convinces without costing anyone cleanup
   1. List the demonstration options available for the claim, from read-only to state-changing.
   2. Rank them by invasiveness, putting observation first, reversible writes second, side effects last.
   3. Select the lowest-ranked option that still satisfies your declared success criteria.
   4. Verify the chosen technique still produces evidence strong enough for a skeptical reviewer.
   5. Document why higher-invasiveness options were rejected, so the choice reads as deliberate.
   6. Re-check the choice if the first technique fails to demonstrate, rather than escalating automatically.

encoding-layer-awareness  (match 2)
  Track how many times your input is encoded and decoded between what you send and what arrives, so the proof targets the value that actually reaches the destination rather than the one you typed
   1. Map each transformation layer between sender and destination: transport encoding, escaping and parsing.
   2. Write the value at every stage, showing exactly how it changes at each hop.
   3. Identify where the destination performs its final decode, since that is the value it will interpret.
   4. Construct the input so it reaches the destination in the intended form after all layers are applied.
   5. Verify by observation: capture what arrived rather than trusting your transformation arithmetic.
   6. Record the layer map with the proof so a reviewer can replay the reasoning.

marker-uniqueness-generation  (match 2)
  Generate markers with enough entropy and a dating convention that collisions with real content are practically impossible and every marker can be traced to its test
   1. Include a date and a random component in every marker so it is both unique and locatable in time.
   2. Draw the random component from a real source with enough bits that collision is not a concern.
   3. Add a short test identifier so a marker maps back to a specific proof without a lookup table.
   4. Check the composed marker against recent captured content to confirm no pre-existing occurrence.
   5. Register the marker in the test record before use, so it exists on record before it appears anywhere.
   6. Keep one registry across tests so repeated or overlapping markers are detected before deployment.

payload-self-validation  (match 2)
  Validate the proof against your own control before executing it live, catching malformed structure, dead markers and wrong assumptions while the cost of being wrong is still zero
   1. Parse your own proof mechanically where possible: structure, encoding and required fields.
   2. Run it against a control condition where the correct outcome is known in advance.
   3. Confirm the marker is findable in your own captured output before searching for it elsewhere.
   4. Check the proof against every constraint you recorded: length, context, delimiters and preconditions.
   5. Fix any failure now, since a live execution that fails teaches you only that your prep was incomplete.
   6. Record the self-validation result so the execution is known to have run against a checked proof.

reviewer-legible-payload-authoring  (match 2)
  Author proofs whose every element a reviewer can explain, so the submission reads as an engineering demonstration rather than an opaque recipe copied from somewhere
   1. Annotate each element of the proof with the job it performs in the demonstration.
   2. Replace unexplained magic values with ones whose purpose is evident from the string itself.
   3. Split compound elements so each line carries exactly one responsibility.
   4. State the intended effect of each annotated element next to the observed effect.
   5. Cut elements that serve no purpose in the demonstration, which only add review noise.
   6. Read the annotated proof as a reviewer would and mark anything you cannot explain in seconds.

## deliver

injection-point-selection  (match 3)
  Select the exact parameter, header or field where the proof enters, naming why that point reaches the behavior under test, so evidence maps to a specific entry the fix can address
   1. List candidate entry points that plausibly reach the component named in your hypothesis.
   2. Rank them by how directly they reach it, preferring points with the shortest unobstructed path.
   3. Check each candidate for transformations that would alter your proof before arrival.
   4. Pick one primary point and name a backup, since a single point can be blocked or filtered.
   5. Record the selection with the reason, so the report ties the observation to a concrete entry.
   6. Re-select deliberately if the primary point fails, rather than silently spraying every candidate.

session-state-hygiene-during-tests  (match 2)
  Control cookies, tokens and cached state during the proof so the identity you think you are testing is the identity actually being tested, run after run
   1. Identify every state carrier your proof touches: cookies, tokens, local storage and server-side sessions.
   2. Reset or isolate that state before each run so the identity under test is unambiguous.
   3. Verify which identity the server actually saw, from the response rather than from your client's assumption.
   4. Separate the two sides of a boundary test into distinct clean sessions with no shared carriers.
   5. Watch for state leaking between runs through caches or reuse of an earlier client instance.
   6. Record the session setup with the evidence so a reviewer knows which identity produced which response.

control-and-test-pairing  (match 1)
  Run a control request alongside every test request under identical conditions, so the difference between them is the evidence and normal behavior is never in dispute
   1. Define the control: identical request with the one variable under test returned to its normal value.
   2. Send control and test in the same session, environment and time window to limit drift.
   3. Capture both responses in full: status, headers and body, at the same fidelity.
   4. Diff the captures and mark which differences are attributable to the single changed variable.
   5. Attach both captures and the diff to the evidence so the claim can be audited without rerunning.
   6. Repeat the pair if any condition changed between runs, since a stale pair proves nothing new.

parameter-channel-routing  (match 1)
  Know which channel carries your proof into the application, query string, body, header, cookie or path, since the channel determines both the transformation applied and the fix required
   1. Identify the channel the real application uses for this value in normal operation.
   2. Confirm your proof travels the same channel, since a different channel may take a different path.
   3. Check whether each candidate channel applies its own parsing, length limit or normalization.
   4. Note which channel your selected injection point uses and what that implies for transformation.
   5. Test one channel at a time rather than mirroring the value across all of them at once.
   6. Record channel results separately, since identical values can behave differently by channel.
