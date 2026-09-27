# Benchmark results overview

Condensed from the full per-query run files in `benchmark_results/`
(gitignored, ~1.6 MB each). Every run scores the same 776 LegalBench-RAG
queries (194 per benchmark) with character-level precision and recall; see
`RESULTS.md` for the method.

## Overall

| Run | Precision | Recall | F1 | Chars returned / query |
|---|---:|---:|---:|---:|
| baseline-rcts-500-ownsplitter | 5.9% | 30.4% | 9.9% | 3,044 |
| baseline-rcts-500 | 5.9% | 31.2% | 9.9% | 3,076 |
| B-hybrid-bm25 | 4.1% | 21.7% | 6.9% | 3,059 |

## Recall by benchmark

| Run | contractnli | cuad | maud | privacy_qa |
|---|---:|---:|---:|---:|
| baseline-rcts-500-ownsplitter | 37.5% | 34.7% | 9.4% | 40.2% |
| baseline-rcts-500 | 40.0% | 34.6% | 9.8% | 40.4% |
| B-hybrid-bm25 | 33.8% | 21.3% | 5.0% | 26.9% |

## Precision by benchmark

| Run | contractnli | cuad | maud | privacy_qa |
|---|---:|---:|---:|---:|
| baseline-rcts-500-ownsplitter | 5.4% | 5.8% | 2.4% | 10.1% |
| baseline-rcts-500 | 5.5% | 5.8% | 2.2% | 10.1% |
| B-hybrid-bm25 | 4.8% | 3.6% | 1.4% | 6.4% |

## Files

- `summary.json`: per-benchmark and overall metrics for every run.
- `sample_results.json`: for each run, the highest- and lowest-recall query in
  each benchmark, with the spans it retrieved.
