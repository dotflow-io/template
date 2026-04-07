"""Post-generation hook: flatten project and fetch cloud templates."""

import os
import shutil
import tempfile
from pathlib import Path

TEMPLATE_BASE_URL = (
    "https://raw.githubusercontent.com/dotflow-io/template/master/cloud"
)

project_dir = Path(os.getcwd())
parent_dir = project_dir.parent
cloud = "{{ cookiecutter.cloud }}"
project_name = "{{ cookiecutter.project_name }}"
module_name = "{{ cookiecutter.module_name }}"

PLACEHOLDER_PROJECT = "{" + "{PROJECT_NAME}" + "}"
PLACEHOLDER_MODULE = "{" + "{MODULE_NAME}" + "}"

# Step 1: Move all generated files to parent directory
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

# Step 2: Fetch cloud templates if a platform was selected
if cloud != "none":
    try:
        from urllib.request import urlopen
        import json

        registry_url = f"{TEMPLATE_BASE_URL}/registry.json"
        registry = json.loads(urlopen(registry_url, timeout=10).read())

        platform = registry["platforms"].get(cloud)
        if platform:
            for filename in platform["files"]:
                url = f"{TEMPLATE_BASE_URL}/{cloud}/{filename}"
                content = urlopen(url, timeout=10).read().decode()
                content = content.replace(PLACEHOLDER_PROJECT, project_name)
                content = content.replace(PLACEHOLDER_MODULE, module_name)
                filepath = parent_dir / filename
                filepath.write_text(content)
    except Exception as err:
        print(f"Warning: Could not fetch cloud templates: {err}")
