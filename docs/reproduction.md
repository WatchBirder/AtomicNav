# Reproduction notes

## Evaluation cohort

The included development table uses the R2R `val_unseen` development cohort with 100 instruction episodes (95 physical routes). The planner receives three human route annotations where the protocol specifies them. Each row is evaluated on the same paired episode set.

This is an integration and ablation study. It is not the official single-instruction R2R leaderboard protocol and should not be reported as such.

## Metrics

- **SR**: task success rate.
- **SPL**: success weighted by path length.
- **OSR**: oracle success rate under the recorded trajectory.
- **NE**: final navigation error in metres.

The executor, camera configuration, action budget, and stopping policy are held fixed within each paired comparison. Executor swaps are explicitly labelled because they are not equivalent policies.

## Local reporting

The committed table is self-contained:

```bash
python scripts/summarize_results.py results/ablation_dev100.csv
```

Full reproduction additionally requires private simulator assets, model weights, and the matching environment. Those assets are not redistributed here and no credentials are read from this repository.

## Release policy

Before a public code release, verify dataset and checkpoint licenses, remove private benchmark annotations, pin the environment, and publish raw traces only when redistribution is permitted.
