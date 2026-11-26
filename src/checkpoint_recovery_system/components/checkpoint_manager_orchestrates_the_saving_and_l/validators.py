"""Pre- and post-conditions for Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process..

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.config import CheckpointManagerOrchestratesTheSavingAndLConfig
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.errors import CheckpointManagerOrchestratesTheSavingAndLContractViolation
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.models import CheckpointManagerOrchestratesTheSavingAndLInput


def validate_input(ctx, config: CheckpointManagerOrchestratesTheSavingAndLConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise CheckpointManagerOrchestratesTheSavingAndLContractViolation(
            "too many candidates for checkpoint_manager_orchestrates_the_saving_and_l",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: CheckpointManagerOrchestratesTheSavingAndLInput, config: CheckpointManagerOrchestratesTheSavingAndLConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise CheckpointManagerOrchestratesTheSavingAndLContractViolation("duplicate candidate ids after checkpoint_manager_orchestrates_the_saving_and_l")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise CheckpointManagerOrchestratesTheSavingAndLContractViolation(
                "checkpoint_manager_orchestrates_the_saving_and_l introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise CheckpointManagerOrchestratesTheSavingAndLContractViolation("checkpoint_manager_orchestrates_the_saving_and_l produced an unsorted ranking")
