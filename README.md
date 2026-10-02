# Code benchmarks (downloaded 2026-10-01)

This repo got too large, so the data now lives in separate repos. This repo keeps the index and `download.py`.

| Repo | Dirs | Size |
|---|---|---|
| [code-benchmarks-python](https://github.com/chihyu-wang-tsmc/code-benchmarks-python) | HumanEval, MBPP, MBXP_mxeval, MathQA-Python | ~43MB |
| [code-benchmarks-competitive](https://github.com/chihyu-wang-tsmc/code-benchmarks-competitive) | APPS, CodeContests, LiveCodeBench | ~110MB |
| [code-benchmarks-bigcodebench](https://github.com/chihyu-wang-tsmc/code-benchmarks-bigcodebench) | BigCodeBench, BigCodeBench-Hard | ~19MB |
| [code-benchmarks-swe-bench](https://github.com/chihyu-wang-tsmc/code-benchmarks-swe-bench) | SWE-bench/{full,Lite,Verified} | ~21MB |
| [code-benchmarks-codexglue](https://github.com/chihyu-wang-tsmc/code-benchmarks-codexglue) | CodeXGLUE/* (12 tasks, all except BigCloneBench) | ~202MB |
| [code-benchmarks-codexglue-bigclonebench](https://github.com/chihyu-wang-tsmc/code-benchmarks-codexglue-bigclonebench) | CodeXGLUE/code_x_glue_cc_clone_detection_big_clone_bench | ~438MB |

## Sources

| Dir | Source | Notes |
|---|---|---|
| HumanEval | hf: openai/openai_humaneval | test 164 |
| MBPP | hf: google-research-datasets/mbpp | full test 500, sanitized test 257 (+train/val/prompt) |
| APPS | hf: codeparrot/apps | test 5000, train 5000 |
| CodeContests | hf: deepmind/code_contests | test 165, valid 117 only; train (7.5G) not downloaded |
| LiveCodeBench | hf: livecodebench/code_generation_lite | test5.jsonl (v5 new, 167) + test6.jsonl (v6 new, 175) only; test.jsonl~test4.jsonl (3.8G) not downloaded |
| BigCodeBench / -Hard | hf: bigcode/bigcodebench(-hard) | v0.1.4: 1140 / 148 |
| SWE-bench/{full,Lite,Verified} | hf: princeton-nlp/SWE-bench, princeton-nlp/SWE-bench_Lite, SWE-bench/SWE-bench_Verified | test 2294 / 300 / 500 |
| CodeXGLUE/* | hf: google/code_x_glue_* (13 tasks) | test + validation only; train not downloaded |
| MBXP_mxeval | github: amazon-science/mxeval | data/mbxp (13 languages), multilingual_humaneval, multilingual_mathqa |
| MathQA-Python | hf: dtruong46me/mathqa-python (community mirror, generated with google/trax) | train 19209, test 1883, challenge_test 403 |

Re-download / add the omitted splits: see download.py (allow_patterns / ignore_patterns).

## Files over GitHub's 100MB limit

`APPS/test.jsonl`, `APPS/train.jsonl`, `LiveCodeBench/test5.jsonl`, `LiveCodeBench/test6.jsonl`
(in code-benchmarks-competitive) and `SWE-bench/full/data/train-00000-of-00001.parquet` (in code-benchmarks-swe-bench)
are not committed. Each of those repos has its own `fetch_large_files.py`; `python fetch_large_files.py` here still
downloads all of them into this layout.
