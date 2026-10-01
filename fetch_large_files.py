"""補抓 code_benchmarks 裡因為超過 GitHub 100MB 上限而沒有放進這個 repo 的大檔。

用法：python fetch_large_files.py
"""
from huggingface_hub import snapshot_download

JOBS = [
    ("APPS", "codeparrot/apps", ["test.jsonl", "train.jsonl"]),
    ("LiveCodeBench", "livecodebench/code_generation_lite", ["test5.jsonl", "test6.jsonl"]),
    ("SWE-bench/full", "princeton-nlp/SWE-bench", ["data/train-00000-of-00001.parquet"]),
]
for local_dir, repo, files in JOBS:
    snapshot_download(repo, repo_type="dataset", local_dir=local_dir, allow_patterns=files)
    print("OK", local_dir, files)
