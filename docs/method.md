# Method

## Problem setting

Standard RGB vision-and-language navigation couples route interpretation and low-level action selection inside one policy. AtomicNav exposes a narrow interface between these responsibilities: a planner proposes a short semantic subgoal, and an executor carries it out from the current physical state.

## Planner

At time `t`, the planner receives:

- the route instruction;
- the current RGB observation;
- a causal record of completed subgoals and their observed outcomes;
- the available human route annotations when the protocol provides multiple descriptions.

It returns one next subgoal rather than a long action sequence. The subgoal is written in terms of a visible landmark, a direction, or a room transition and ends with an explicit observable condition.

## Executor

The executor is an RGB navigation policy with its own action loop and local stopping behavior. It receives only the active atomic subgoal and the visual observations required by its policy. It outputs navigation actions until it emits `STOP` or reaches the configured action budget.

## Handoff

At a local `STOP`, AtomicNav records the reached state and the stopping evidence. The planner then decides whether the subgoal is complete, needs a corrective subgoal, or should be replaced. The physical pose is preserved; a subtask transition is not a simulator reset.

## Design principle

The interface is deliberately semantic and low bandwidth:

```text
instruction + RGB history → short subgoal
short subgoal + RGB stream → actions + local STOP
local STOP + reached state → next subgoal
```

This lets the planner change without retraining the executor, and lets different RGB executors be compared under the same planner protocol.
