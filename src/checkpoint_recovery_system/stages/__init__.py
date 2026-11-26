"""Role implementations. Components specialise one of these strategies."""

from checkpoint_recovery_system.stages.answer import AnswerStage
from checkpoint_recovery_system.stages.approval import ApprovalStage
from checkpoint_recovery_system.stages.audit import AuditStage
from checkpoint_recovery_system.stages.base import Stage, StageServices
from checkpoint_recovery_system.stages.budget import BudgetStage
from checkpoint_recovery_system.stages.cache import CacheStage
from checkpoint_recovery_system.stages.enrich import EnrichStage
from checkpoint_recovery_system.stages.fallback import FallbackStage
from checkpoint_recovery_system.stages.ingest import IngestStage
from checkpoint_recovery_system.stages.policy import PolicyStage
from checkpoint_recovery_system.stages.retrieve import RetrieveStage
from checkpoint_recovery_system.stages.score import ScoreStage

ROLE_CLASSES: dict[str, type[Stage]] = {
    "ingest": IngestStage,
    "retrieve": RetrieveStage,
    "enrich": EnrichStage,
    "score": ScoreStage,
    "cache": CacheStage,
    "policy": PolicyStage,
    "budget": BudgetStage,
    "approval": ApprovalStage,
    "fallback": FallbackStage,
    "audit": AuditStage,
    "answer": AnswerStage,
}

__all__ = ["ROLE_CLASSES", "Stage", "StageServices", *[cls.__name__ for cls in ROLE_CLASSES.values()]]
