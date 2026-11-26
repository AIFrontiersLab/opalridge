"""Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process..

Blends upstream prior scores with query-aware relevance and reorders candidates.
"""

from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.adapter import ROLE, build
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.config import CONFIG, CheckpointManagerOrchestratesTheSavingAndLConfig
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.errors import CheckpointManagerOrchestratesTheSavingAndLError
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.service import CheckpointManagerOrchestratesTheSavingAndLService

__all__ = ["CONFIG", "ROLE", "build", "CheckpointManagerOrchestratesTheSavingAndLConfig", "CheckpointManagerOrchestratesTheSavingAndLError", "CheckpointManagerOrchestratesTheSavingAndLService"]
