"""Errors raised by Storage System: A reliable and scalable storage solution that supports atomic file operations to ensure checkpoint integrity.. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from checkpoint_recovery_system.kernel.errors import StageError


class StorageSystemAReliableAndScalableStorageSError(StageError):
    code = "storage_system_a_reliable_and_scalable_storage_s_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("storage_system_a_reliable_and_scalable_storage_s", message, retryable=retryable, details=details)


class StorageSystemAReliableAndScalableStorageSContractViolation(StorageSystemAReliableAndScalableStorageSError):
    code = "storage_system_a_reliable_and_scalable_storage_s_contract_violation"
