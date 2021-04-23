"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""

import os
from pathlib import Path
from typing import Callable, Optional


def get_paths(dir_path: Path, file_extension: str):
    names = os.path.basename(f"{dir_path}.{file_extension}")
    yield names


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    result = 0
    if tokenizer is None:
        tokenizer = lambda x: x.split("\n")
    paths = get_paths(dir_path, file_extension)
    for path in paths:
        with open(path) as f:
            result += sum(1 for _ in tokenizer(f.read()))
    return result
