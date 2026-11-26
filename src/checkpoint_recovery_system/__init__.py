"""Checkpoint Recovery System: governed reference service.

Building a Robust Checkpoint Recovery System for LLM Training

Public entry points:

* ``build_container`` - wire the full object graph from settings.
* ``run`` - execute a single request and return the outcome as a dict.
"""

from checkpoint_recovery_system.application.pipeline import run
from checkpoint_recovery_system.container import build_container
from checkpoint_recovery_system.version import __version__

__all__ = ["__version__", "build_container", "run"]
