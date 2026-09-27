"""Minimal AtomicNav planner--executor handoff example.

This example is dependency-free. Replace ``Planner`` and ``Executor`` with
adapters for your VLM and RGB navigation policy; the handoff protocol stays
the same across implementations.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass
class AtomicSubgoal:
    """A short intention paired with an observable completion condition."""

    instruction: str
    completion: str
    scope: str = "INTERMEDIATE"


@dataclass
class Handoff:
    """State returned by the executor at a local boundary."""

    observation: Any
    reached_state: dict[str, Any] = field(default_factory=dict)
    stop_evidence: str = ""


class Planner(Protocol):
    def next_subgoal(
        self,
        route_instruction: str,
        observation: Any,
        memory: list[dict[str, Any]],
    ) -> AtomicSubgoal: ...


class Executor(Protocol):
    def run(self, subgoal: AtomicSubgoal, observation: Any) -> Handoff: ...


def run_atomicnav_episode(
    route_instruction: str,
    initial_observation: Any,
    planner: Planner,
    executor: Executor,
    *,
    max_subgoals: int = 32,
) -> Handoff:
    """Compose local executions while preserving the physical state."""

    observation = initial_observation
    memory: list[dict[str, Any]] = []

    for _ in range(max_subgoals):
        subgoal = planner.next_subgoal(route_instruction, observation, memory)
        handoff = executor.run(subgoal, observation)
        memory.append(
            {
                "instruction": subgoal.instruction,
                "completion": subgoal.completion,
                "scope": subgoal.scope,
                "reached_state": handoff.reached_state,
                "stop_evidence": handoff.stop_evidence,
            }
        )
        observation = handoff.observation
        if subgoal.scope == "FINAL":
            return handoff

    raise RuntimeError("max_subgoals reached before a FINAL subgoal")


if __name__ == "__main__":
    print("AtomicNav interface example loaded.")
    print("Connect a general VLM planner and an RGB executor to run an episode.")
