# Ledger templates

Read this file only after the learner has enabled persistent tracking and a ledger
location is known.

## questions.md

```markdown
# Questions

## Grading
- **P0** — blocks the next meaningful action or current decision
- **P1** — progress is possible, but the current choice cannot be explained
- **P2** — no effect on a current action or decision

States: `open`, `answered-unverified`, `verified`, `dropped`

Entry format:
- [P1][answered-unverified] Why did this effect run again?
  Raised: YYYY-MM-DD / context
  Current understanding: none
  Promotes when: observable condition; required for P2, omit otherwise
  Guessed: if a guess was made
  Answer summary: concise answer already given
  Learner explanation: required for verified
  Verified: date, or blank

---

## Open

## Answered — unverified

## Verified

## Dropped
<!-- Retain inactive P2s with a reason. -->
```

## observations.md

```markdown
# Observations

### [N] One-line summary
- When: YYYY-MM-DD / context
- Expected:
- Actual:
- Guess:
- Follow-up: linked question or resolution
```

## Review output

```markdown
## Review — YYYY-MM-DD

Open: P0 n / P1 n / P2 n
Answered — unverified: n
Verified since last review: n
Promoted: [question] — condition met
Dropped: [question] — reason
Re-verified: [question] — passed / reopened
```
