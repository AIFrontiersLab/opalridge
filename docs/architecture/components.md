# Components (C4 level 3)

| # | Stage | Role | Critical | Source |
|---|---|---|---|---|
| 1 | `intake` (Intake) | `ingest` | yes | built-in |
| 2 | `corpus_retrieval` (Corpus Retrieval) | `retrieve` | no | built-in |
| 3 | `storage_system_a_reliable_and_scalable_storage_s` (Storage System: A reliable and scalable storage solution that supports atomic file operations to ensure checkpoint integrity.) | `enrich` | no | [component](../components/storage_system_a_reliable_and_scalable_storage_s.md) |
| 4 | `ranking_cache` (Ranking Cache) | `cache` | no | [component](../components/ranking_cache.md) |
| 5 | `checkpoint_manager_orchestrates_the_saving_and_l` (Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process.) | `score` | no | [component](../components/checkpoint_manager_orchestrates_the_saving_and_l.md) |
| 6 | `recovery_module_ensures_that_the_model_can_be_re` (Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility.) | `score` | no | [component](../components/recovery_module_ensures_that_the_model_can_be_re.md) |
| 7 | `graceful_fallback` (Graceful Fallback) | `fallback` | no | built-in |
| 8 | `access_policy` (Access Policy) | `policy` | yes | built-in |
| 9 | `token_budget_governor` (Token Budget Governor) | `budget` | no | [component](../components/token_budget_governor.md) |
| 10 | `audit_recorder` (Audit Recorder) | `audit` | no | [component](../components/audit_recorder.md) |
| 11 | `answer_assembly` (Answer Assembly) | `answer` | yes | built-in |

Each concept component follows the same internal layout so reviewers can navigate
any of them blind: `config.py`, `port.py`, `service.py`, `validators.py`, `models.py`,
`metrics.py`, `errors.py`, `adapter.py`.
