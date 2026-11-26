"""Contract tests for the Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process. component (role: score)."""

import pytest

from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l import CONFIG, ROLE, build
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.errors import CheckpointManagerOrchestratesTheSavingAndLContractViolation
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.models import CheckpointManagerOrchestratesTheSavingAndLInput, CheckpointManagerOrchestratesTheSavingAndLReport
from checkpoint_recovery_system.components.checkpoint_manager_orchestrates_the_saving_and_l.validators import validate_input, validate_output
from checkpoint_recovery_system.domain.models import Candidate, PipelineContext, Request


def _ctx(candidates, **request):
    req = Request.from_dict({"query": "evidence retrieval policy", **request})
    return PipelineContext(run_id="run_test", request=req, candidates=candidates)


def _cands():
    return [
        Candidate("d1", "evidence retrieval policy overview", prior_score=0.9, score=0.9, classification="public"),
        Candidate("d2", "unrelated cooking notes", prior_score=0.5, score=0.5, classification="internal"),
        Candidate("d3", "retrieval evidence and policy controls", prior_score=0.7, score=0.7, classification="internal"),
    ]


def test_role_and_name(services):
    stage = build(services)
    assert ROLE == "score"
    assert stage.name == CONFIG.name == "checkpoint_manager_orchestrates_the_saving_and_l"
    assert stage.describe()["display_name"] == 'Checkpoint Manager: Orchestrates the saving and loading of model states using a background thread to avoid blocking the main training process.'


def test_process_records_report(services):
    stage = build(services)
    ctx = _ctx(_cands())
    stage.process(ctx)
    report = ctx.metadata["reports"]["checkpoint_manager_orchestrates_the_saving_and_l"]
    assert report["stage"] == "checkpoint_manager_orchestrates_the_saving_and_l"
    assert report["candidates_in"] == 3
    assert services.metrics.counter("component_checkpoint_manager_orchestrates_the_saving_and_l_runs_total") == 1


def test_output_has_no_duplicate_ids(services):
    stage = build(services)
    ctx = _ctx(_cands())
    stage.process(ctx)
    ids = [c.doc_id for c in ctx.candidates]
    assert len(ids) == len(set(ids))


def test_input_bound_is_enforced():
    from dataclasses import replace

    ctx = _ctx(_cands())
    with pytest.raises(CheckpointManagerOrchestratesTheSavingAndLContractViolation):
        validate_input(ctx, replace(CONFIG, max_input_candidates=1))


def test_unknown_ids_rejected_unless_allowed():
    from dataclasses import replace

    ctx = _ctx(_cands())
    before = CheckpointManagerOrchestratesTheSavingAndLInput(query="q", candidate_ids=("d1",))
    strict = replace(CONFIG, may_introduce_ids=False, enforce_sorted_output=False)
    with pytest.raises(CheckpointManagerOrchestratesTheSavingAndLContractViolation):
        validate_output(ctx, before, strict)
    validate_output(ctx, before, replace(strict, may_introduce_ids=True))


def test_report_diff():
    report = CheckpointManagerOrchestratesTheSavingAndLReport.diff("checkpoint_manager_orchestrates_the_saving_and_l", CheckpointManagerOrchestratesTheSavingAndLInput("q", ("a", "b")), ["b", "c"])
    assert report.added == ("c",)
    assert report.removed == ("a",)
    assert report.to_dict()["candidates_out"] == 2
