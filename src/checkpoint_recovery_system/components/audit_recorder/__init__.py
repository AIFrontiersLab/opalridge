"""Audit Recorder.

Writes a hash-chainable audit record for every run, including denials and degradations.
"""

from checkpoint_recovery_system.components.audit_recorder.adapter import ROLE, build
from checkpoint_recovery_system.components.audit_recorder.config import CONFIG, AuditRecorderConfig
from checkpoint_recovery_system.components.audit_recorder.errors import AuditRecorderError
from checkpoint_recovery_system.components.audit_recorder.service import AuditRecorderService

__all__ = ["CONFIG", "ROLE", "build", "AuditRecorderConfig", "AuditRecorderError", "AuditRecorderService"]
