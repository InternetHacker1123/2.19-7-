from datetime import datetime
import pathlib

directory = pathlib.Path.cwd()

time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
print(datetime.fromtimestamp(time), file_path)
