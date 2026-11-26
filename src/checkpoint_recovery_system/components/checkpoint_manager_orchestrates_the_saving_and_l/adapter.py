"""Port and registry adapter for Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process..

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.config import CONFIG
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.service import CheckpointManagerOrchestratesTheSavingAndLService
from checkpoint_recovery_system.domain.models import PipelineContext

ROLE = CONFIG.role


class CheckpointManagerOrchestratesTheSavingAndLPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> CheckpointManagerOrchestratesTheSavingAndLService:
    return CheckpointManagerOrchestratesTheSavingAndLService(services)
