"""Port and registry adapter for Storage System: A reliable and scalable storage solution that supports atomic file operations to ensure checkpoint integrity..

Interface from the architecture specification: ``process(ctx) -> None``
"""

from __future__ import annotations

from typing import Protocol

from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.config import CONFIG
from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.service import StorageSystemAReliableAndScalableStorageSService
from checkpoint_recovery_system.domain.models import PipelineContext

ROLE = CONFIG.role


class StorageSystemAReliableAndScalableStorageSPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> StorageSystemAReliableAndScalableStorageSService:
    return StorageSystemAReliableAndScalableStorageSService(services)
