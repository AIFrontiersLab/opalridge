# Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility.

Blends upstream prior scores with query-aware relevance and reorders candidates.

| Property | Value |
|---|---|
| Stage name | `recovery_module_ensures_that_the_model_can_be_re` |
| Role | `score` |
| Interface | `process(ctx) -> None` |
| Critical | No. A failure degrades the run and downstream fallback restores a safe ordering. |
| Origin | architecture specification |

## Files

| File | Purpose |
|---|---|
| `config.py` | Frozen configuration dataclass and defaults |
| `service.py` | `RecoveryModuleEnsuresThatTheModelCanBeReService` (role strategy plus contract checks) and metric recording |
| `validators.py` | Pre/post conditions (bounded input, no duplicate or unknown ids, ordering) |
| `models.py` | Input snapshot and per-run report |
| `errors.py` | Component error types (all `StageError` subclasses) |
| `adapter.py` | Port protocol and the factory registered in the stage registry |

## Behaviour

Blends upstream prior scores with query-aware relevance and reorders candidates.

See also [`docs/components/recovery_module_ensures_that_the_model_can_be_re.md`](../../../../docs/components/recovery_module_ensures_that_the_model_can_be_re.md).
