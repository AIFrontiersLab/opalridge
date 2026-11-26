"""Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility..

Blends upstream prior scores with query-aware relevance and reorders candidates.
"""

from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.adapter import ROLE, build
from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.config import CONFIG, RecoveryModuleEnsuresThatTheModelCanBeReConfig
from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.errors import RecoveryModuleEnsuresThatTheModelCanBeReError
from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.service import RecoveryModuleEnsuresThatTheModelCanBeReService

__all__ = ["CONFIG", "ROLE", "build", "RecoveryModuleEnsuresThatTheModelCanBeReConfig", "RecoveryModuleEnsuresThatTheModelCanBeReError", "RecoveryModuleEnsuresThatTheModelCanBeReService"]
