# Granite local experiments: research log

This log describes user-run Granite 4.1 3B experiments supplied in this archive. No new model inference was performed during consolidation. The timestamps in directory names are UTC; the user session occurred on October 31, 2026 in Atlantic time. These are small exploratory diagnostics, not broad capability estimates.

## Planning and writing

The model produced readable plans, essays, and screenplay drafts. A planning revision claiming a three-hour budget allocated 300 minutes. The screenplay opened an explicitly protected sealed envelope in both draft and revision, and failed to implement the changed knowledge asymmetry. The essay correction changed the number and wording without explicitly discussing the smaller evidential difference. Word ranges were often missed. These are qualitative observations; prose quality is not assigned an automatic score.

## Targeted correction

A targeted schedule repair correctly allocated 180 minutes, then labeled a 105-minute allocation as 120 minutes. An isolated audit correctly identified 105, the false claim, budget compliance, and 15 unused minutes. The early mixed prose excerpt showed inconsistent judgments despite correct additions; only A–C were supplied at that stage, so missing D–F were not counted as failures.

## Matched audit runs

The JSON run is `granite-audit-tests/audit-runs/20261101T011057.562911Z`; the prose run is `granite-audit-tests/audit-runs/20261101T011303.582436Z`. Both used seed 42. Prose scores below are manual semantic judgments, not original runner scores. Original response files and scores are preserved unchanged.

| Condition | Entire cases correct | Sums correct |
|---|---:|---:|
| JSON individual | 0/6 | 1/6 |
| JSON batch | 2/6 | 4/6 |
| Prose individual | 5/6 | 5/6 |
| Prose batch | 4/6 | 6/6 |

The individual prose error was E: the response wrote 70 + 20 = 110 and propagated that total into the remainder. The batched prose errors were claim correctness in D and F; both matching claims were rejected despite correct sums and remainders. Individual A's unusual label “Neutral” is treated as correct because its explanation explicitly identifies equality with the budget. The JSON batch passed B and C completely. Valid JSON and correct field types were returned in every JSON request.

The console's old REVIEW/FAIL label was misleading for prose: prose was never automatically graded. This update prints MANUAL REVIEW for prose and case counts for structured responses. Existing saved scores retain their original meaning and are not rewritten.

Prose was more accurate in these runs, but the prompts changed in both format and explicit calculation instructions. One seed and six fixed cases do not isolate a cause or establish a general rate. The initial hypothesis that independent requests improve accuracy was not supported in JSON and was supported only descriptively in this prose run.

## Fictional flood puzzle

The response shortened a four-minute telephone call to three minutes, omitted the action that stops the leak, and inconsistently labeled a five-minute move as 6–9 while describing completion at 11. It nevertheless declared success. A valid original schedule is valve 0–3, unlock 3–4, electricity 4–6, move 6–11. In the alternative, the minute-6 leak deadline conflicts with the plumber stopping it at minute 9. The response reached impossibility but did not clearly isolate that conflict. The direct CLI output contains terminal escape sequences; the original is retained.

The puzzle explicitly states that an ongoing leak past minute 6 ruins the boxes. This unconditional rule is the basis for evaluating the alternative; it should not be silently reinterpreted as allowing early evacuation to defeat that deadline. The earlier test discussion also anticipated an impossible alternative, so it was not an unprimed impossibility test.

## JSON with intermediate sums

The third audit run is `granite-audit-tests/audit-runs/20261101T013857.751926Z`, supplied as `granite-json-steps-results.tar.gz`. It used Granite 4.1 3B, seed 42, and the `json-steps` style. No new inference was performed in reviewing it.

All six individual responses and all six batched cases contained correct cumulative-sum arrays. Every individual response omitted the required `id` field, so all six correctly failed strict schema-based scoring. When manually associated with their single-case input, five of the six had correct values for all four final answer fields. This contextual assessment does not convert a schema failure into a strict pass. Individual B correctly calculated 105 but incorrectly reported an overrun and a remainder of -15, rather than no overrun and +15.

The batch included all IDs and passed the requested shape. A, C, and F were entirely correct. B's running totals ended at 105, but its `actual_sum` was 120; E's running totals ended at 90, but its `actual_sum` was 100. In both cases, the final total matched the supplied claimed total instead of the computed total. D correctly calculated 135 but incorrectly rejected the matching claim of 135. Thus all intermediate arrays were correct, while only four final totals and three complete batched answers were correct.

| Measure | Plain JSON | Prose | JSON with steps |
|---|---:|---:|---:|
| Individual final sums correct | 1/6 | 5/6 | 6/6 |
| Individual final judgments all correct, assessed in context | 0/6 | 5/6 | 5/6 |
| Batched final sums correct | 4/6 | 6/6 | 4/6 |
| Batched cases entirely correct | 2/6 | 4/6 | 3/6 |

For the last column, individual final-answer correctness ignores missing IDs only for manual semantic assessment. Strict individual passes remain 0/6. Prose has no strict JSON-schema score. Intermediate arrays add another requirement and should not be conflated with final sums; their accuracy in the JSON-with-steps run was 6/6 individually and 6/6 in the batch.

## Interpretation and limits

In these samples, explicit intermediate arithmetic was associated with better individual sum accuracy than final-answer-only JSON. Correct intermediate values did not ensure correct final fields or relational judgments. The batched JSON-with-steps output directly exhibits correct calculations followed by contradictory final totals. This supports distinguishing calculation accuracy, agreement between intermediate and final values, claim verification, budget interpretation, and schema compliance when reading the results.

These are descriptive findings from six fixed cases at one seed per condition. Prompt wording, output format, and generated length differ across conditions. The results do not establish a causal explanation, a general model capability rate, or access to the model's internal reasoning. No further experiments or script changes are included in this log update.

