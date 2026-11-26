"""Extension points: stage factories and lifecycle hooks."""

from checkpoint_recovery_system.plugins.hooks import HookManager
from checkpoint_recovery_system.plugins.registry import StageRegistry

__all__ = ["HookManager", "StageRegistry"]
