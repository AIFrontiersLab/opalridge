"""Storage System: A reliable and scalable storage solution that supports atomic file operations to ensure checkpoint integrity..

Annotates candidates with structural features and collapses exact duplicates.
"""

from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.adapter import ROLE, build
from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.config import CONFIG, StorageSystemAReliableAndScalableStorageSConfig
from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.errors import StorageSystemAReliableAndScalableStorageSError
from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.service import StorageSystemAReliableAndScalableStorageSService

__all__ = ["CONFIG", "ROLE", "build", "StorageSystemAReliableAndScalableStorageSConfig", "StorageSystemAReliableAndScalableStorageSError", "StorageSystemAReliableAndScalableStorageSService"]
