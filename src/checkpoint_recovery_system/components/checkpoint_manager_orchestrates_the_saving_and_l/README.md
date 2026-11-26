# Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process.

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage name | `checkpoint_manager_orchestrates_the_saving_and_l` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | No. A failure degrades the run and downstream fallback restores a safe ordering. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `CheckpointManagerOrchestratesTheSavingAndLService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Blends upstream prior scores with query-aware relevance and reorders candidates.

See also [`docs/components/checkpoint_manager_orchestrates_the_saving_and_l.md`](../../../../docs/components/checkpoint_manager_orchestrates_the_saving_and_l.md).
