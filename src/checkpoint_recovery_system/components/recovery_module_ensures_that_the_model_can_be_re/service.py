"""Recovery Module: Ensures that the model can be restored to the exact state of the last verified checkpoint, including optimizer states and RNG seeds for reproducibility. service.

Role: ``score``. Blends upstream prior scores with query-aware relevance and reorders candidates.

Responsibility (from the architecture specification):
    Blends upstream prior scores with query-aware relevance and reorders candidates.

The service specialises :class:`ScoreStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.config import CONFIG, RecoveryModuleEnsuresThatTheModelCanBeReConfig
from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.models import RecoveryModuleEnsuresThatTheModelCanBeReInput, RecoveryModuleEnsuresThatTheModelCanBeReReport
from checkpoint_recovery_system.components.recovery_module_ensures_that_the_model_can_be_re.validators import validate_input, validate_output
from checkpoint_recovery_system.stages.score import ScoreStage

METRIC_PREFIX = "component_recovery_module_ensures_that_the_model_can_be_re"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: RecoveryModuleEnsuresThatTheModelCanBeReReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class RecoveryModuleEnsuresThatTheModelCanBeReService(ScoreStage):
    def __init__(self, services, config: RecoveryModuleEnsuresThatTheModelCanBeReConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = RecoveryModuleEnsuresThatTheModelCanBeReInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = RecoveryModuleEnsuresThatTheModelCanBeReReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = RecoveryModuleEnsuresThatTheModelCanBeReReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
