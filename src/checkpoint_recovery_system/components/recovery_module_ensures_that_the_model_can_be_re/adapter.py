"""Port and registry adapter for Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility..

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.config import CONFIG
from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.service import RecoveryModuleEnsuresThatTheModelCanBeReService
from checkpoint_recovery_system.domain.models import PipelineContext

ROLE = CONFIG.role


class RecoveryModuleEnsuresThatTheModelCanBeRePort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> RecoveryModuleEnsuresThatTheModelCanBeReService:
    return RecoveryModuleEnsuresThatTheModelCanBeReService(services)
