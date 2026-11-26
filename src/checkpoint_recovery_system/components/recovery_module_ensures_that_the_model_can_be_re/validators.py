"""Pre- and post-conditions for Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility..

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.config import RecoveryModuleEnsuresThatTheModelCanBeReConfig
from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.errors import RecoveryModuleEnsuresThatTheModelCanBeReContractViolation
from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.models import RecoveryModuleEnsuresThatTheModelCanBeReInput


def validate_input(ctx, config: RecoveryModuleEnsuresThatTheModelCanBeReConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise RecoveryModuleEnsuresThatTheModelCanBeReContractViolation(
            "too many candidates for recovery_module_ensures_that_the_model_can_be_re",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: RecoveryModuleEnsuresThatTheModelCanBeReInput, config: RecoveryModuleEnsuresThatTheModelCanBeReConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise RecoveryModuleEnsuresThatTheModelCanBeReContractViolation("duplicate candidate ids after recovery_module_ensures_that_the_model_can_be_re")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise RecoveryModuleEnsuresThatTheModelCanBeReContractViolation(
                "recovery_module_ensures_that_the_model_can_be_re introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise RecoveryModuleEnsuresThatTheModelCanBeReContractViolation("recovery_module_ensures_that_the_model_can_be_re produced an unsorted ranking")
