"""Pre- and post-conditions for Storage System: A reliable and scalable storage solution that supports atomic file operations to ensure checkpoint integrity..

Violations are defects, not transient faults, so they are raised as
non-retryable errors and surface as a degraded (or failed, if critical) stage.
"""

from __future__ import annotations

from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.config import StorageSystemAReliableAndScalableStorageSConfig
from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.errors import StorageSystemAReliableAndScalableStorageSContractViolation
from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.models import StorageSystemAReliableAndScalableStorageSInput


def validate_input(ctx, config: StorageSystemAReliableAndScalableStorageSConfig) -> None:
    if len(ctx.candidates) > config.max_input_candidates:
        raise StorageSystemAReliableAndScalableStorageSContractViolation(
            "too many candidates for storage_system_a_reliable_and_scalable_storage_s",
            details={"limit": config.max_input_candidates, "received": len(ctx.candidates)},
        )


def validate_output(ctx, before: StorageSystemAReliableAndScalableStorageSInput, config: StorageSystemAReliableAndScalableStorageSConfig) -> None:
    ids = [c.doc_id for c in ctx.candidates]
    if len(ids) != len(set(ids)):
        raise StorageSystemAReliableAndScalableStorageSContractViolation("duplicate candidate ids after storage_system_a_reliable_and_scalable_storage_s")
    if not config.may_introduce_ids:
        unexpected = set(ids) - set(before.candidate_ids)
        if unexpected:
            raise StorageSystemAReliableAndScalableStorageSContractViolation(
                "storage_system_a_reliable_and_scalable_storage_s introduced unknown candidates", details={"ids": sorted(unexpected)}
            )
    if config.enforce_sorted_output and not ctx.cache_hit:
        scores = [c.score for c in ctx.candidates]
        if scores != sorted(scores, reverse=True):
            raise StorageSystemAReliableAndScalableStorageSContractViolation("storage_system_a_reliable_and_scalable_storage_s produced an unsorted ranking")
