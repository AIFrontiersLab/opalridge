# Getting started

1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -e ".[dev]"`
3. `make test`
4. `python -m checkpoint_recovery_system run examples/requests/governed_query.json`
5. `python -m checkpoint_recovery_system serve` and `curl -s localhost:8080/v1/pipeline`
