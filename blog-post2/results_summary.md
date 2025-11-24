## Experiment Results Summary

### Experimental Setup

- **Model**: meta-llama/Llama-3.1-8B-Instruct
- **Datasets**: Spec-Bench and BlazeEdit
- **Tree depth**: 64
- **Speculation length**: 32
- **Trials per configuration**: 3
- **Concurrency levels**: 1, 4, 16, 64
- **Baselines**:
  - Vanilla (no speculative decoding)
  - N-gram [3, 5] and [5, 5] (prompt lookup decoding)
  - Suffix matching (old and new implementations)
- **Metric**: Mean Time Per Output Token (TPOT) in milliseconds, averaged across trials

### Blazedit

| Baseline | Concurrency 1 | Concurrency 4 | Concurrency 16 | Concurrency 64 |
|----------|------------------|------------------|------------------|------------------|
| vanilla | 5.61 | 5.99 | 7.46 | 11.12 |
| ngram [3, 5] | 1.86 | 2.16 | 3.40 | 7.99 |
| ngram [5, 5] | 2.17 | 2.50 | 3.59 | 7.42 |
| suffix_old | 1.71 | 1.99 | 3.02 | 6.58 |
| suffix_new | 1.71 | 1.92 | 2.86 | 6.06 |

### Spec Bench

| Baseline | Concurrency 1 | Concurrency 4 | Concurrency 16 | Concurrency 64 |
|----------|------------------|------------------|------------------|------------------|
| vanilla | 5.53 | 5.80 | 6.75 | 10.48 |
| ngram [3, 5] | 5.21 | 5.49 | 6.80 | 13.14 |
| ngram [5, 5] | 5.63 | 5.83 | 6.91 | 11.57 |
| suffix_old | 4.46 | 4.78 | 6.23 | 12.11 |
| suffix_new | 4.43 | 4.70 | 5.92 | 10.96 |

