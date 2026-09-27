# Benchmark dataset samples

A small slice of [LegalBench-RAG](https://github.com/zeroentropy-ai/legalbenchrag)
showing the format the evaluator consumes. The full dataset is not stored in
this repo; download it and set `LEGALBENCH_DIR` (see the top-level README).

Each `<benchmark>/tests.json` has the same schema as the upstream
`benchmarks/<benchmark>.json`: a query plus ground-truth snippets, where `span`
is a `[start, end)` character range into the source document.

| Benchmark | Tests upstream | Sampled | Source document(s) |
|---|---:|---:|---|
| contractnli | 977 | 3 | `contractnli/Focus-Group-APIC-Seattle-Confidentiality-Agreement-031115.txt` (in `corpus/`) |
| cuad | 4,042 | 3 | `cuad/NETZEEINC_11_14_2002-EX-10.3-MAINTENANCE AGREEMENT.txt` (in `corpus/`) |
| maud | 1,676 | 3 | `maud/Magellan Health, Inc._Centene Corporation.txt`, `maud/Raven Industries, Inc._CNH Industrial N.V..txt` (too large to include; each snippet carries a `context_excerpt` instead) |
| privacy_qa | 194 | 3 | `privacy_qa/Keep.txt` (in `corpus/`) |

Documents in `corpus/` are unmodified copies, so the spans index into them directly.
