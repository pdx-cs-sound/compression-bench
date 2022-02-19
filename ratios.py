from collections import defaultdict
import os, stat, sys

exts = [
    ".gz",
    ".xz",
    ".zstd",
    ".flac",
    ".flacq",
    ".ape",
    ".m4a",
    ".als",
    ".baco",
    ".mp3",
]
ext_index = set(exts)

sizes = defaultdict(dict)

for f in os.scandir("audio"):
    base, wav = os.path.splitext(f.path)
    if wav != ".wav":
        continue
    base = os.path.split(base)[-1]
    fstat = os.stat(f.path)
    size = fstat[stat.ST_SIZE]
    sizes[base][wav[1:]] = size

for f in os.scandir("compressed"):
    base, ext = os.path.splitext(f.path)
    if ext not in exts:
        continue
    base = os.path.split(base)[-1]
    fstat = os.stat(f.path)
    size = fstat[stat.ST_SIZE]
    sizes[base][ext[1:]] = size

for f in sorted(list(sizes)):
    print(f)
    baseline = None
    if "wav" in sizes[f]:
        baseline = sizes[f]["wav"]
    for e in exts:
        if e[1:] not in sizes[f]:
            print(f"  {f} {e}: missing")
        else:
            size = sizes[f][e[1:]]
            name = f"{f}{e}:".rjust(30)
            ratio = ""
            if baseline != None:
                ratio = f"{baseline / size:-5.2f}×"
            print(f"{name} {size:-7} {ratio}")
