"""Ports: the interfaces the application core requires from the outside world.

Adapters under ``checkpoint_recovery_system.adapters`` implement these protocols. The core never
imports an adapter directly; the composition root (``container.py``) wires them.
"""

from checkpoint_recovery_system.ports.audit import AuditSink
from checkpoint_recovery_system.ports.cache import RankingCache
from checkpoint_recovery_system.ports.corpus import CorpusRepository
from checkpoint_recovery_system.ports.event_bus import EventBus
from checkpoint_recovery_system.ports.repository import RunRepository
from checkpoint_recovery_system.ports.scorer import RelevanceScorer

__all__ = ["AuditSink", "CorpusRepository", "EventBus", "RankingCache", "RelevanceScorer", "RunRepository"]
