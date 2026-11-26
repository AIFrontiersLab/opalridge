"""Ranking Cache.

Short-circuits repeated identical requests with a TTL-bounded ranking cache keyed by principal.
"""

from checkpoint_recovery_system.components.ranking_cache.adapter import ROLE, build
from checkpoint_recovery_system.components.ranking_cache.config import CONFIG, RankingCacheConfig
from checkpoint_recovery_system.components.ranking_cache.errors import RankingCacheError
from checkpoint_recovery_system.components.ranking_cache.service import RankingCacheService

__all__ = ["CONFIG", "ROLE", "build", "RankingCacheConfig", "RankingCacheError", "RankingCacheService"]
