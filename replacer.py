#!/bin/python
"""Globally replace 'target' for a given 'repl' on import statements. Also changes files and folders,
and uses GAWK to process files."""

from pathlib import Path
import sys
import os
from glob import glob
import re

try:
    target, repl = sys.argv[1:]
except ValueError as e:
    print(""">>> python3 replacer.py [target] [repl]\n""")
    print(e)
assert len(repl) > 1, repl

paths = map(Path, glob(str(Path.cwd() / "**/*"), recursive=True))
paths = sorted(paths, key=lambda p: len(str(p).split("/")), reverse=True)
# files = filter(lambda f: f.split("/")[-1] !==*stuff goes here*, files)

for path in paths:
    if not path.is_dir():
        # -i inplace : made the modifications in sito
        # -v set the variable "repl" to {repl}
        os.system(f"awk -i inplace -v target={target} -v repl={repl} -f script.awk {path}")
    path.rename(path.parent / str(path.name).replace(target, repl))
