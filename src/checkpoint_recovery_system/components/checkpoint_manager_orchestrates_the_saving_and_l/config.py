"""Static configuration for the Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process. component."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CheckpointManagerOrchestratesTheSavingAndLConfig:
    name: str = "checkpoint_manager_orchestrates_the_saving_and_l"
    display_name: str = 'Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process.'
    role: str = "score"
    interface: str = 'process(ctx) -> None'
    responsibility: str = 'Blends upstream prior scores with query-aware relevance and reorders candidates.'
    max_input_candidates: int = 10_000
    may_introduce_ids: bool = False
    enforce_sorted_output: bool = True


CONFIG = CheckpointManagerOrchestratesTheSavingAndLConfig()
