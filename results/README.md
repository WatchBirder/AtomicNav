# Results provenance

`ablation_dev100.csv` contains the completed rows exported from the internal ablation ledger on 2026-09-27. Every row contains 100 episodes from the same development cohort.

Interpretation:

- `full_online` is the current AtomicNav reference: Astra planner, causal task memory, and the v6 RGB executor.
- `offline` generates the initial task list once and does not revise it online.
- `no_memory` removes cross-subtask memory while preserving the local executor loop.
- `text_memory` keeps only the textual handoff state.
- The executor rows replace the RGB executor while keeping the planner protocol as fixed as possible.
- The language-model rows replace the planner; they are not claims that one model is universally better.
- `official_whole` is a released whole-route reference and is not an AtomicNav planner–executor run.

These results are exploratory. The cohort is small, planner annotations are part of the development protocol, and the table is not directly comparable to official leaderboard numbers.
