---
name: knowledge-debt
description: Use when a learner explicitly wants to keep a persistent questions log, knowledge-gap journal, or prioritized record of deferred learning questions across sessions.
---

# Knowledge Debt

Maintain a prioritized ledger of unanswered, deferred, and verified learning
questions. The core distinction is **postponed versus abandoned**.

## Activation and consent

Use persistent tracking only when the learner explicitly requests it or accepts a
brief offer. Do not activate merely because someone wants an explanation, is
debugging, or says they want to learn.

Before creating or changing files:

1. Confirm that the learner wants persistent tracking.
2. Ask where the ledger should live if no location was designated.
3. Treat existing files as the ledger only when the learner identifies them as such.

If tracking is declined, answer normally, create no files, and do not ask again in
the current task. Without an active ledger, never withhold an answer for later.

If the learner pauses or withdraws tracking, stop ledger reads, writes, and offers
immediately. Preserve existing files unchanged and reactivate only on a new explicit
request.

With an active ledger, read its known files before modifying them. An urgent or
blocked learner is the exception: unblock first and update the ledger afterward
only if it remains relevant.

## Triage active-ledger questions

Classify internally before answering.

| Grade | Test | Default action |
|---|---|---|
| **P0** | Blocks the next meaningful action or current decision | Answer now, then log |
| **P1** | Progress is possible, but the learner cannot explain or defend the current choice | Answer briefly, log as `answered-unverified` |
| **P2** | Has no effect on a current action or decision | Log and defer with a promotion condition |

Announce a grade conversationally only when deferring, promoting, or when the
learner asks. Grades remain metadata in the ledger. Defer a P1 only with the
learner's agreement. If they say “just tell me,” answer; log it only when the
ledger is already active.

Split topic-sized prompts into concrete questions before grading them.

## Guess first, selectively

Ask for one brief guess only when all of these hold:

- the question is causal or judgment-based;
- the learner has enough evidence to form a hypothesis;
- they are not blocked, rushed, or frustrated; and
- the interaction is learning-first rather than outcome-first.

“No idea” or “just tell me” ends the prompt immediately. Answer factual, syntax,
API-shape, and error-meaning questions directly.

## Recording and resolution

When output differs from expectation, capture `Expected`, `Actual`, and `Guess`.
Never manufacture an observation. Read [references/templates.md](references/templates.md)
before creating or changing ledger files.

Use four states:

- `open` — unanswered or deliberately deferred;
- `answered-unverified` — answered, but not explained by the learner;
- `verified` — correctly explained in the learner's own words;
- `dropped` — inactive P2 retained with a reason.

When the learner says they understand, invite a one- or two-sentence teach-back.
If it is incorrect, materially incomplete, or declined, keep `answered-unverified`;
do not interrogate them. Preserve a wrong guess beside the later explanation.

## Rhythm

- At the start of a later session with a known active ledger, surface only questions
  relevant to the current work.
- Run an end review only when the learner is wrapping up or the learning task ends.
- Run a periodic review only on request or through an automation the learner has
  approved.

Read [references/ledger-operations.md](references/ledger-operations.md) when setting
up a ledger, adding or updating an entry, changing states, or conducting a review. Read
[references/dialogues.md](references/dialogues.md) when response shape is unclear.

## Common mistakes

- Activating on ordinary tutoring or routine debugging
- Asking for file locations before the learner chooses persistent tracking
- Announcing P0/P1 on every answer
- Deferring without an active ledger
- Asking for guesses while the learner is blocked or rushed
- Treating “makes sense” as verified understanding
- Letting review rituals interrupt the learner's current task
