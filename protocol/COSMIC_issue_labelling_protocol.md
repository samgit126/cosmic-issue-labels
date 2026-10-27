# COSMIC issue-labelling protocol (v0.1, 27 October 2026)

Purpose: assign a functional size in COSMIC function points (CFP) to an issue-tracker item (story, task, bug) from its title and description alone, in a way two trained raters can reproduce. Based on the COSMIC Measurement Manual v5.0 and the agile guideline of the COSMIC consortium.

## 0. Inputs and decision to size

Read title and description. Decide first:

- **Functional change?** The issue adds, changes or removes behaviour visible to a functional user (a human, another system, a scheduler). Pure refactoring, build, configuration, documentation and test-only work are **not functional**: label `sizeable = no`, `reason = non-functional`.
- **Enough information?** If the text does not let you name at least one functional process and its data movements, label `sizeable = no`, `reason = insufficient-text`. Do not guess from the issue key or the project.

## 1. Identify the functional user(s) and the triggering event

Who or what sends or receives the data? Record the functional user type: `human`, `system`, `timer`. The triggering event is what starts the process (a click, an incoming message, a schedule).

## 2. Identify the functional processes

One functional process = one triggering event + everything the software does in response until it is complete. A single issue often holds one process; "and also" sentences may hold several. List each. A bug fix that changes behaviour is sized as the process it changes, counting only the data movements the fix touches.

## 3. Identify data groups

A data group is a set of attributes about one object of interest (an order, a user, an executor, a slave). Name them; each distinct object of interest is one data group.

## 4. Count data movements per functional process

| Type | Code | Count one when |
|---|---|---|
| Entry | E | a data group moves from a functional user into the process (input, incoming message, event payload) |
| Exit | X | a data group moves from the process out to a functional user (display, response, error message, notification) |
| Read | R | the process reads a data group from persistent storage |
| Write | W | the process writes/updates/deletes a data group in persistent storage |

Rules that matter most for issues:

- Each **distinct data group** moved in a given direction counts **once** per process, however many attributes it has.
- An error/confirmation message to the user is **one Exit** per process, not one per error.
- Reading the same data group twice in one process is one Read.
- A triggering Entry always exists: every process has at least 1 E and, in practice, at least 1 X or W. Minimum size of a sizeable process is 2 CFP.
- Do not count control commands with no data (a "Cancel" with no payload).

## 5. Compute the size

`CFP(issue) = Σ over functional processes (E + X + R + W)`. Record the per-type totals as well.

## 6. Confidence and notes

Record `rater_confidence` on 1–3 (1 = guessed from thin text, 2 = text supports most movements, 3 = text is explicit) and a one-line `notes` field naming the processes.

## 7. Two-rater procedure

Raters work blind. Disagreements of more than 1 CFP, or any disagreement on `sizeable`, go to adjudication where both raters re-read the issue together and record the agreed value with `adjudicated = yes`. Report Cohen's κ for `sizeable`, and ICC(2,1) plus mean absolute difference for CFP.

## 8. Known limits

Sizing from text alone under-counts Reads and Writes that an implementer discovers only in the code. The labels therefore measure the *specified* functional size of the issue, which is the quantity available before work starts and the one the companion paper needs.
