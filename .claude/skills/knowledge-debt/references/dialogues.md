# Response examples

## Ordinary explanation: do not activate

> **Learner:** Explain why `useEffect` can loop. I want to understand it.

> **Response:** `useEffect` runs after rendering. If it changes a dependency, that
> change causes another render and the effect runs again. The cycle continues until
> the update is guarded or the dependency becomes stable.

No grade, guess prompt, file question, or ledger offer is necessary.

## Explicit activation

> **Learner:** Keep track of what I don't know while I study.

> **Response:** I can maintain a persistent questions ledger and an observations
> log. Where should they live?

Tracking was explicitly requested, so asking for a location is appropriate.

## Deferring a P2

> **Learner:** Why is PostgreSQL more popular than other databases?

> **Response:** That's P2 for today's work—it won't change the current database
> decision. I logged it to revisit when you need to justify the choice or consider
> migration. Back to the vector column.

Announce the grade only because an active-ledger question is being deferred.

## Guess first: causal and unblocked

> **Learner:** Antonyms are scoring 0.82. Why?

> **Response:** What's your guess based on the examples you've run? One sentence is
> enough; then I'll explain.

Ask once. “No idea” receives the answer immediately.

## No guess for factual questions

> **Learner:** What's the cosine operator in pgvector?

> **Response:** `<=>`. For example: `ORDER BY embedding <=> query_vec LIMIT 5`.

## Urgent override

> **Learner:** Production is failing. Just tell me why this API returns 500.

> **Response:** Send the matching server log or stack trace and the endpoint code;
> I'll identify the cause directly.

Do not announce a grade, request a learning guess, or interrupt with ledger setup.
If an active ledger exists, record the question afterward only if it matters to the
learner's continuing study.

## Answered but not verified

> **Learner:** That makes sense, but I don't want to summarize it now.

> **Response:** No problem. I'll leave it as answered but unverified.

Teach-back is an invitation, not a condition for ending the conversation.

## Verified

> **Learner:** Embeddings learn from surrounding words, so antonyms can be close
> because they occur in similar contexts.

> **Response:** Logged as verified in your own words.
