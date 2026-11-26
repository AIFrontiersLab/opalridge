"""Stage catalog for Checkpoint Recovery System.

Declares the default stage order and registers every built-in and component stage
with the plugin registry. Imports of stage classes are deferred so configuration
modules can read ``DEFAULT_STAGE_ORDER`` without import cycles.
"""

from __future__ import annotations

DEFAULT_STAGE_ORDER = [
    "intake",
    "corpus_retrieval",
    "storage_system_a_reliable_and_scalable_storage_s",
    "ranking_cache",
    "checkpoint_manager_orchestrates_the_saving_and_l",
    "recovery_module_ensures_that_the_model_can_be_re",
    "graceful_fallback",
    "access_policy",
    "token_budget_governor",
    "audit_recorder",
    "answer_assembly",
]

BUILTINS = {
    "intake": "ingest",
    "corpus_retrieval": "retrieve",
    "relevance_scoring": "score",
    "access_policy": "policy",
    "graceful_fallback": "fallback",
    "answer_assembly": "answer",
}

COMPONENTS = [
    {"name": 'Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process.', "slug": "checkpoint_manager_orchestrates_the_saving_and_l", "role": "score", "origin": "spec"},
    {"name": 'Storage System: A reliable and scalable storage solution that supports atomic file operations to ensure checkpoint integrity.', "slug": "storage_system_a_reliable_and_scalable_storage_s", "role": "enrich", "origin": "spec"},
    {"name": 'Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility.', "slug": "recovery_module_ensures_that_the_model_can_be_re", "role": "score", "origin": "spec"},
    {"name": 'Ranking Cache', "slug": "ranking_cache", "role": "cache", "origin": "padded"},
    {"name": 'Token Budget Governor', "slug": "token_budget_governor", "role": "budget", "origin": "padded"},
    {"name": 'Audit Recorder', "slug": "audit_recorder", "role": "audit", "origin": "padded"},
]


def register_all(registry) -> None:
    from checkpoint_recovery_system.components import COMPONENT_FACTORIES
    from checkpoint_recovery_system.stages import ROLE_CLASSES

    for name, role in BUILTINS.items():
        cls = ROLE_CLASSES[role]
        registry.register(name, role, lambda services, cls=cls, name=name: cls(name, services), source="builtin")
    for name, (role, factory) in COMPONENT_FACTORIES.items():
        registry.register(name, role, factory, source="component")
