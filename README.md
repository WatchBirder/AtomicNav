<div align="center">

# AtomicNav

### Generalist VLM planning with reusable atomic RGB navigation execution

A small planner–executor interface for vision-and-language navigation. A generalist VLM chooses the next semantic subgoal; an RGB navigation policy carries it out and returns a local completion signal.

<p>
  <a href="docs/method.md">Method</a> ·
  <a href="docs/reproduction.md">Reproduction notes</a> ·
  <a href="CITATION.cff">Citation</a>
</p>

</div>

<p align="center">
  <img src="assets/overview.png" alt="AtomicNav: generalist planning and shared RGB execution" width="100%" />
</p>

The public repository is a compact project page for the paper. It documents the method and its integration boundary while the implementation package is being prepared for release.

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

## Code release

The training, evaluation, model-integration, and runtime code will be added to the [`code/`](code/) folder in a later release. It is intentionally not included in this research snapshot. The current repository therefore does not claim to be a runnable benchmark package.

## What is included

```text
assets/overview.png       paper-style overview figure
assets/architecture.svg   lightweight interface diagram
code/                     reserved for the future code release
docs/                     method and reproduction notes
```

The repository excludes private datasets, simulator assets, checkpoints, raw traces, internal paths, benchmark tables, and credentials. The `code/` directory is a placeholder for the future release package.

## Documentation

- [`docs/method.md`](docs/method.md) — problem setting, planner, executor, and handoff semantics.
- [`docs/reproduction.md`](docs/reproduction.md) — release boundary and requirements for a full run.
- [`docs/demo.md`](docs/demo.md) — public demo and redistribution notes.
- [`NOTICE.md`](NOTICE.md) — third-party and redistribution notices.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). The paper title and author list remain provisional until the public release.

<div align="center">

[![Research snapshot](https://img.shields.io/badge/release-research%20snapshot-orange?style=flat-square)](https://github.com/WatchBirder/AtomicNav)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

</div>



