import pathlib

directory = pathlib.Path.cwd()

max((f.stat().st_mtime, f) for f in directory.iterdir())[1].read_text()
