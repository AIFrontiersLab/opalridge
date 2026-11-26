# Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility.

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage | `recovery_module_ensures_that_the_model_can_be_re` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/checkpoint_recovery_system/components/recovery_module_ensures_that_the_model_can_be_re/` |
| Tests | `tests/unit/components/test_component_recovery_module_ensures_that_the_model_can_be_re.py` |

## Behaviour

Blends upstream prior scores with query-aware relevance and reorders candidates.

## Contract

- Input is bounded by `max_input_candidates`.
- Output contains no duplicate ids.
- Never introduces candidate ids that were not in its input.
- Output is sorted by descending score.

## On failure

Run degrades; fallback restores upstream prior order.

## Metrics

- `component_recovery_module_ensures_that_the_model_can_be_re_runs_total`
- `component_recovery_module_ensures_that_the_model_can_be_re_candidates_out` (histogram)
- `component_recovery_module_ensures_that_the_model_can_be_re_removed_total`
