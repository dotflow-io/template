"""Post-generation hook: move all files up one level into the parent directory."""

import os
import shutil
import tempfile
from pathlib import Path

project_dir = Path(os.getcwd())
parent_dir = project_dir.parent

with tempfile.TemporaryDirectory() as tmp:
    tmp_dir = Path(tmp)

    for item in project_dir.iterdir():
        shutil.move(str(item), str(tmp_dir / item.name))

    project_dir.rmdir()

    for item in tmp_dir.iterdir():
        dest = parent_dir / item.name
        if dest.exists():
            if dest.is_dir():
                shutil.rmtree(dest)
            else:
                dest.unlink()
        shutil.move(str(item), str(dest))
