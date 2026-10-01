from huggingface_hub import snapshot_download, HfApi
import os
B = os.path.expanduser("~/code_benchmarks")
jobs = [
    ("HumanEval",            "openai/openai_humaneval", None),
    ("MBPP",                 "google-research-datasets/mbpp", None),
    ("APPS",                 "codeparrot/apps", None),
    ("CodeContests",         "deepmind/code_contests", ["*test*", "*valid*", "README.md", "dataset_infos.json"]),
    ("BigCodeBench",         "bigcode/bigcodebench", None),
    ("BigCodeBench-Hard",    "bigcode/bigcodebench-hard", None),
    ("SWE-bench/full",       "princeton-nlp/SWE-bench", None),
    ("SWE-bench/Lite",       "princeton-nlp/SWE-bench_Lite", None),
    ("SWE-bench/Verified",   "SWE-bench/SWE-bench_Verified", None),
    ("MathQA-Python",        "dtruong46me/mathqa-python", None),
]
for d in HfApi().list_datasets(author="google", search="code_x_glue"):
    jobs.append((f"CodeXGLUE/{d.id.split('/')[1]}", d.id, None))
for name, repo, allow in jobs:
    ignore = ["*train*"] if name.startswith("CodeXGLUE") else None
    p = snapshot_download(repo, repo_type="dataset", local_dir=f"{B}/{name}",
                          allow_patterns=allow, ignore_patterns=ignore)
    print("OK", name, flush=True)
