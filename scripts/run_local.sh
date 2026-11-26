#!/usr/bin/env bash
set -euo pipefail
export CHECKPOINT_RECOVERY_SYSTEM_CONFIG=${CHECKPOINT_RECOVERY_SYSTEM_CONFIG:-config/development.toml}
PYTHONPATH=src exec python -m checkpoint_recovery_system serve "$@"
