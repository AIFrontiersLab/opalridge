# Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process.

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage | `checkpoint_manager_orchestrates_the_saving_and_l` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | no |
| Source | `src/checkpoint_recovery_system/components/checkpoint_manager_orchestrates_the_saving_and_l/` |
| Tests | `tests/unit/components/test_component_checkpoint_manager_orchestrates_the_saving_and_l.py` |

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

- `component_checkpoint_manager_orchestrates_the_saving_and_l_runs_total`
- `component_checkpoint_manager_orchestrates_the_saving_and_l_candidates_out` (histogram)
- `component_checkpoint_manager_orchestrates_the_saving_and_l_removed_total`
