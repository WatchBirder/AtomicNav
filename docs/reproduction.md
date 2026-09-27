# Reproduction notes

This repository is a lightweight public snapshot of the AtomicNav interface. It does not contain the simulator, benchmark assets, model weights, or service credentials.

## Local example

The dependency-free example exercises the public planner--executor handoff:

```bash
python examples/semantic_handoff.py
```

To run a real navigation experiment, connect a planner adapter and an RGB executor adapter as described in [`examples/semantic_handoff.py`](../examples/semantic_handoff.py). The adapter boundary is intentionally small so that the planner and executor can be replaced independently.

## Full reproduction

A complete run additionally requires a compatible RGB navigation environment, licensed scene data, model checkpoints, and the matching runtime configuration. Those assets are maintained separately and are not redistributed in this repository.

Before any public benchmark release, verify dataset and checkpoint licenses, pin the environment, document the observation and action protocol, and publish only traces and media whose terms permit redistribution.
