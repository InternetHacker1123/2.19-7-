import collections
import pathlib

collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir())
