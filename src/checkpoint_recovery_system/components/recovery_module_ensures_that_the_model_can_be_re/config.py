"""Static configuration for the Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility. component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RecoveryModuleEnsuresThatTheModelCanBeReConfig:
    name: str = "recovery_module_ensures_that_the_model_can_be_re"
    display_name: str = 'Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility.'
    role: str = "score"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Blends upstream prior scores with query-aware relevance and reorders candidates.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = True


CONFIG = RecoveryModuleEnsuresThatTheModelCanBeReConfig()
