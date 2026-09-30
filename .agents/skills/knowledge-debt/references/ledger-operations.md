# Ledger operations

Read this reference only when persistent tracking is active and the current task
requires setup, adding or updating an entry, a state transition, or a review.

## Setup

1. Confirm persistent tracking and the destination.
2. If designated ledger files exist, read them and preserve the learner's edits.
3. If they do not exist, create `questions.md` and `observations.md` from
   [templates.md](templates.md).
4. State what was created or changed.

Do not adopt unrelated files merely because they have matching names. If writing is
unavailable, show the proposed entry inline and let the learner decide where to save
it.

## Adding an entry

Search for the same underlying question before adding a duplicate. If found, update
its context, grade, or promotion condition. Otherwise record the minimum fields the
current state needs; blank optional fields are acceptable.

Organize entries by state section (`Open`, `Answered — unverified`, `Verified`, or
`Dropped`) and keep P0/P1/P2 as entry metadata. Move one entry when its state changes;
never duplicate it across grade and state sections.

For surprises, record:

```text
Expected: what the learner predicted
Actual: what occurred
Guess: their current hypothesis, including “none”
```

## State transitions

- New deferred question → `open`
- Answer supplied → `answered-unverified`
- Learner explains it correctly in their own words → `verified`
- Explanation is incorrect or materially incomplete → `answered-unverified`
- Re-verification fails → `answered-unverified`
- Inactive P2 is intentionally retired → `dropped` with a reason
- A dropped question becomes relevant again → move it to `open` and reassess its grade

Never mark an item `verified` merely because the learner heard or recognized the
answer. Do not force a teach-back when they decline.

When a P2 promotion condition is met, reassess it against the current work. Assign
P0, P1, or P2 again and follow that grade's default action. Move a dropped item to
`open` first; otherwise preserve its state until answering or verification causes a
state transition.

## Session boundaries

At a later session start, surface an old item only when it affects the current work.
At task completion or an explicit wrap-up, briefly ask about new questions,
observations, and possible verification. Do not insert a review ritual into an
ongoing or urgent task.

## Periodic review

Run only when requested or through an approved automation:

1. Promote P2s whose observable condition now holds.
2. Invite re-explanation of one or two verified items; reopen failures as
   `answered-unverified`.
3. Move stale P2s with no continuing value to `dropped`; retain the reason.
4. Report compact counts by grade and state.

Treat six weeks or roughly forty open items as review prompts, not automatic rules.
