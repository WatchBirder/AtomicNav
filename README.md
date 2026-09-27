<div align="center">

# AtomicNav

### Generalist VLM planning with reusable atomic RGB navigation execution

A small planner–executor interface for vision-and-language navigation. A generalist VLM chooses the next semantic subgoal; an RGB navigation policy carries it out and returns a local completion signal.

<p>
  <a href="docs/method.md">Method</a> ·
  <a href="docs/reproduction.md">Reproduction notes</a> ·
  <a href="results/README.md">Results</a> ·
  <a href="CITATION.cff">Citation</a>
</p>

</div>

<p align="center">
  <img src="assets/overview.png" alt="AtomicNav: generalist planning and shared RGB execution" width="100%" />
</p>

AtomicNav keeps route reasoning and continuous control in separate interfaces. The planner sees the route instruction, the current RGB observation, and causal task memory. It emits one short intention with an observable completion condition. The executor acts from the current physical state until it emits `STOP`; the next planner call resumes from the state that was actually reached.

## The interface

| Planner | Executor |
| --- | --- |
| Reads the full route and tracks progress across subgoals. | Runs the local RGB action loop and resolves visual ambiguity. |
| Emits a semantic subgoal, not a long trajectory. | Emits actions and a local `STOP`. |
| Owns global memory and decides what comes next. | Owns task-local history and completion evidence. |

An atomic subgoal is deliberately simple:

```text
instruction:  "Enter the bedroom and face the chair."
completion:   "Stop fully inside the bedroom, facing the chair."
scope:        "INTERMEDIATE"   # or FINAL
```

The physical state is continuous across subgoals. A local `STOP` returns control to the planner; only a `FINAL` subgoal ends the route.

## Quick start

This public snapshot is documentation-first and dependency-light. It does not bundle the simulator, model weights, benchmark assets, or service credentials.

```bash
git clone https://github.com/WatchBirder/AtomicNav-Research.git
cd AtomicNav-Research

# Run the dependency-free interface example
python examples/semantic_handoff.py

# Summarize the included development table
python scripts/summarize_results.py results/ablation_dev100.csv
```

To connect your own models, implement the two small interfaces shown in [`examples/semantic_handoff.py`](examples/semantic_handoff.py):

```python
class Planner:
    def next_subgoal(self, route_instruction, observation, memory):
        ...  # call your general VLM and return AtomicSubgoal

class Executor:
    def run(self, subgoal, observation):
        ...  # call your RGB navigator and return Handoff
```

The full handoff loop is provided by `run_atomicnav_episode(...)`. The same protocol can wrap different general VLM planners or RGB executors without changing the route-level state machine.

## What is included

```text
assets/overview.png             paper-style overview figure
assets/architecture.svg         lightweight interface diagram
examples/semantic_handoff.py   dependency-free planner/executor API example
configs/                        versioned development configuration
docs/                           method and reproduction notes
results/                        curated aggregate tables
scripts/                        small reporting utilities
```

The repository intentionally excludes private datasets, simulator assets, checkpoints, raw traces, internal paths, and credentials. See [`docs/reproduction.md`](docs/reproduction.md) for the exact release boundary and the benchmark protocol used by the included development table.

## Development snapshot

The included table is a paired 100-episode development cohort for integration and ablation analysis. It is not the official single-instruction R2R leaderboard protocol and should not be read as a standard SOTA claim.

| Variant | SR | SPL | OSR | NE (m) |
| --- | ---: | ---: | ---: | ---: |
| AtomicNav (full online memory) | **79.00** | 63.64 | 87.00 | 2.57 |
| RGB, no cross-subtask memory | 72.00 | 61.93 | 81.00 | 2.87 |
| Initial plan only | 57.00 | 49.38 | 75.00 | 3.63 |

See [`results/ablation_dev100.csv`](results/ablation_dev100.csv) and [`results/README.md`](results/README.md) for all rows, cohort construction, and caveats.

## Documentation

- [`docs/method.md`](docs/method.md) — problem setting, planner, executor, and handoff semantics.
- [`docs/reproduction.md`](docs/reproduction.md) — evaluation cohort, metrics, and release boundary.
- [`docs/demo.md`](docs/demo.md) — notes on public demo media and redistribution limits.
- [`NOTICE.md`](NOTICE.md) — third-party and redistribution notices.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). The paper title and author list remain provisional until the public release.

<div align="center">

[![Research snapshot](https://img.shields.io/badge/release-research%20snapshot-orange?style=flat-square)](https://github.com/WatchBirder/AtomicNav-Research)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

</div>
