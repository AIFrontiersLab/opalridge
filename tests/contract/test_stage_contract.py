"""Every registered stage honours the stage contract on an empty and a populated context."""

import pytest

from checkpoint_recovery_system.domain.models import Candidate, PipelineContext, Request
from checkpoint_recovery_system.plugins.registry import StageRegistry
from checkpoint_recovery_system.stage_catalog import register_all
from checkpoint_recovery_system.stages.base import Stage

REGISTRY = StageRegistry()
register_all(REGISTRY)


@pytest.mark.parametrize("name", REGISTRY.names())
def test_stage_contract(name, services):
    stage = REGISTRY.create(name, services)
    assert isinstance(stage, Stage)
    info = stage.describe()
    assert info["name"] == name and info["role"]
    for candidates in ([], [Candidate("a", "policy text", prior_score=0.5, score=0.5, classification="public")]):
        ctx = PipelineContext(run_id=f"r-{name}", request=Request.from_dict({"query": "policy"}), candidates=list(candidates))
        stage.process(ctx)
        ids = [c.doc_id for c in ctx.candidates]
        assert len(ids) == len(set(ids))
