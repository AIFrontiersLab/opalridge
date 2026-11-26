from checkpoint_recovery_system.domain.models import Candidate, PipelineContext, Request
from checkpoint_recovery_system.stages.enrich import EnrichStage


def test_collapses_duplicates_and_annotates(services):
    ctx = PipelineContext(
        run_id="r",
        request=Request.from_dict({"query": "policy retrieval"}),
        candidates=[Candidate("a", "Policy retrieval!"), Candidate("b", "policy   retrieval"), Candidate("c", "other")],
    )
    EnrichStage("enrich", services).process(ctx)
    assert [c.doc_id for c in ctx.candidates] == ["a", "c"]
    assert ctx.candidates[0].metadata["query_overlap"] == 2
