# Experiment Results Summary

## Experimental Setup

- **Model**: meta-llama/Llama-3.1-8B-Instruct
- **Datasets**: Spec-Bench and BlazeEdit
- **Tree depth**: 64, 32, or 24
- **Speculation length**: 32
- **Trials per configuration**: 3
- **Concurrency levels**: 1, 4, 16, 64
- **Baselines**:
  - Vanilla (no speculative decoding)
  - N-gram [3, 5] and [5, 5] (prompt lookup decoding)
  - Suffix matching (old and new implementations)
- **Metric**: Mean Time Per Output Token (TPOT) in milliseconds, averaged across trials

## Blazedit

| Baseline | Concurrency 1 | Concurrency 4 | Concurrency 16 | Concurrency 64 |
|----------|------------------|------------------|------------------|------------------|
| vanilla | 5.62 | 5.98 | 7.44 | 10.96 |
| ngram [3, 5] | 1.84 | 2.16 | 3.37 | 7.99 |
| ngram [5, 5] | 2.15 | 2.49 | 3.54 | 7.33 |
| suffix_old | 1.69 | 1.95 | 2.99 | 6.54 |
| suffix_new (depth=64) | 1.68 | 1.91 | 2.83 | 5.98 |
| suffix_new (depth=32) | 1.76 | 1.97 | 2.81 | 5.77 |
| suffix_new (depth=24) | 1.80 | 2.01 | 2.79 | 5.58 |

## Spec Bench

| Baseline | Concurrency 1 | Concurrency 4 | Concurrency 16 | Concurrency 64 |
|----------|------------------|------------------|------------------|------------------|
| vanilla | 5.53 | 5.78 | 6.73 | 10.36 |
| ngram [3, 5] | 5.07 | 5.43 | 6.73 | 13.07 |
| ngram [5, 5] | 5.49 | 5.80 | 6.87 | 11.55 |
| suffix_old | 4.33 | 4.76 | 6.20 | 12.03 |
| suffix_new (depth=64) | 4.33 | 4.69 | 5.84 | 10.90 |
| suffix_new (depth=32) | 4.34 | 4.64 | 5.75 | 10.53 |
| suffix_new (depth=24) | 4.32 | 4.62 | 5.70 | 10.37 |

