"""Storage System: A reliable and scalable storage solution that supports atomic file operations to ensure checkpoint integrity. service.

Role: ``enrich``. Annotates candidates with structural features and collapses exact duplicates.

Responsibility (from the architecture specification):
    Annotates candidates with structural features and collapses exact duplicates.

The service specialises :class:`EnrichStage` and wraps it with this
component's contract checks, metrics, and per-run report.
"""

from __future__ import annotations

from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.config import CONFIG, StorageSystemAReliableAndScalableStorageSConfig
from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.models import StorageSystemAReliableAndScalableStorageSInput, StorageSystemAReliableAndScalableStorageSReport
from checkpoint_recovery_system.components.storage_system_a_reliable_and_scalable_storage_s.validators import validate_input, validate_output
from checkpoint_recovery_system.stages.enrich import EnrichStage

METRIC_PREFIX = "component_storage_system_a_reliable_and_scalable_storage_s"
RUNS = f"{METRIC_PREFIX}_runs_total"
CANDIDATES_OUT = f"{METRIC_PREFIX}_candidates_out"
REMOVED = f"{METRIC_PREFIX}_removed_total"


def record_metrics(metrics, report: StorageSystemAReliableAndScalableStorageSReport) -> None:
    if metrics is None:
        return
    metrics.inc(RUNS)
    metrics.observe(CANDIDATES_OUT, report.candidates_out)
    if report.removed:
        metrics.inc(REMOVED, len(report.removed))


class StorageSystemAReliableAndScalableStorageSService(EnrichStage):
    def __init__(self, services, config: StorageSystemAReliableAndScalableStorageSConfig = CONFIG) -> None:
        super().__init__(config.name, services, description=config.responsibility)
        self.config = config

    def process(self, ctx) -> None:
        validate_input(ctx, self.config)
        before = StorageSystemAReliableAndScalableStorageSInput.from_context(ctx)
        super().process(ctx)
        if ctx.halted and not ctx.candidates:
            report = StorageSystemAReliableAndScalableStorageSReport.diff(self.name, before, [], halted=True)
        else:
            validate_output(ctx, before, self.config)
            report = StorageSystemAReliableAndScalableStorageSReport.diff(self.name, before, [c.doc_id for c in ctx.candidates])
        ctx.metadata.setdefault("reports", {})[self.name] = report.to_dict()
        record_metrics(self.services.metrics, report)

    def describe(self) -> dict:
        info = super().describe()
        info.update({"display_name": self.config.display_name, "interface": self.config.interface})
        return info
