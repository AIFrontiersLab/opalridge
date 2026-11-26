"""Concept-specific components. Each one specialises a stage role with its own
configuration, validation, metrics, and errors."""

from checkpoint_recovery_system.components.audit_recorder import adapter as _audit_recorder
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l import adapter as _checkpoint_manager_orchestrates_the_saving_and_l
from checkpoint_recovery_system.components.ranking_cache import adapter as _ranking_cache
from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re import adapter as _recovery_module_ensures_that_the_model_can_be_re
from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s import adapter as _storage_system_a_reliable_and_scalable_storage_s
from checkpoint_recovery_system.components.token_budget_governor import adapter as _token_budget_governor

COMPONENT_FACTORIES = {
    "checkpoint_manager_orchestrates_the_saving_and_l": (_checkpoint_manager_orchestrates_the_saving_and_l.ROLE, _checkpoint_manager_orchestrates_the_saving_and_l.build),
    "storage_system_a_reliable_and_scalable_storage_s": (_storage_system_a_reliable_and_scalable_storage_s.ROLE, _storage_system_a_reliable_and_scalable_storage_s.build),
    "recovery_module_ensures_that_the_model_can_be_re": (_recovery_module_ensures_that_the_model_can_be_re.ROLE, _recovery_module_ensures_that_the_model_can_be_re.build),
    "ranking_cache": (_ranking_cache.ROLE, _ranking_cache.build),
    "token_budget_governor": (_token_budget_governor.ROLE, _token_budget_governor.build),
    "audit_recorder": (_audit_recorder.ROLE, _audit_recorder.build),
}
