"""Errors raised by Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility.. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from checkpoint_recovery_system.kernel.errors import StageError


class RecoveryModuleEnsuresThatTheModelCanBeReError(StageError):
    code = "recovery_module_ensures_that_the_model_can_be_re_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("recovery_module_ensures_that_the_model_can_be_re", message, retryable=retryable, details=details)


class RecoveryModuleEnsuresThatTheModelCanBeReContractViolation(RecoveryModuleEnsuresThatTheModelCanBeReError):
    code = "recovery_module_ensures_that_the_model_can_be_re_contract_violation"
