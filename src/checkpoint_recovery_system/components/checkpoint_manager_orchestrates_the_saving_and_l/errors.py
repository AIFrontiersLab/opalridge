"""Errors raised by Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process.. They are ``StageError`` subclasses so the
orchestrator applies its standard retry, breaker, and fallback semantics."""

from __future__ import annotations

from checkpoint_recovery_system.kernel.errors import StageError


class CheckpointManagerOrchestratesTheSavingAndLError(StageError):
    code = "checkpoint_manager_orchestrates_the_saving_and_l_error"

    def __init__(self, message: str, *, retryable: bool = False, details: dict | None = None) -> None:
        super().__init__("checkpoint_manager_orchestrates_the_saving_and_l", message, retryable=retryable, details=details)


class CheckpointManagerOrchestratesTheSavingAndLContractViolation(CheckpointManagerOrchestratesTheSavingAndLError):
    code = "checkpoint_manager_orchestrates_the_saving_and_l_contract_violation"
