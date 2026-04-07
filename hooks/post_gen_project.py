"""Post-generation hook: fetch cloud templates for the selected platform."""

import json
from pathlib import Path
from urllib.request import urlopen

CLOUD_URL = "https://raw.githubusercontent.com/dotflow-io/template/master/cloud"

CLOUD = "{{ cookiecutter.cloud }}"

SCHEDULED_PLATFORMS = {"lambda-scheduled", "ecs-scheduled", "cloud-run-scheduled"}

PLACEHOLDERS = {
    "PROJECT_NAME": "{{ cookiecutter.project_name }}",
    "MODULE_NAME": "{{ cookiecutter.module_name }}",
    "STACK_NAME": "{{ cookiecutter.project_name | replace('_', '-') }}",
    "K8S_NAME": "{{ cookiecutter.project_name | replace('_', '-') }}",
    "SCHEDULE_EXPRESSION": "{{ cookiecutter.schedule_expression }}",
    "AWS_ACCOUNT_ID": "{{ cookiecutter.aws_account_id }}",
    "AWS_REGION": "{{ cookiecutter.aws_region }}",
    "GCP_PROJECT_ID": "{{ cookiecutter.gcp_project_id }}",
    "GCP_REGION": "{{ cookiecutter.gcp_region }}",
}


def fetch_registry() -> dict:
    content = urlopen(f"{CLOUD_URL}/registry.json", timeout=10).read()
    return json.loads(content)


def fetch_file(platform: str, filename: str) -> str:
    url = f"{CLOUD_URL}/{platform}/{filename}"
    return urlopen(url, timeout=10).read().decode()


def replace_placeholders(content: str) -> str:
    for key, value in PLACEHOLDERS.items():
        tag = "{" + "{" + key + "}" + "}"
        content = content.replace(tag, value)
    return content


def generate_cloud_files():
    if CLOUD == "none":
        return

    registry = fetch_registry()
    platform = registry["platforms"].get(CLOUD)
    if not platform:
        return

    project_dir = Path.cwd()

    for filename in platform["files"]:
        content = fetch_file(CLOUD, filename)
        content = replace_placeholders(content)
        (project_dir / filename).write_text(content)


try:
    generate_cloud_files()
except Exception as err:
    print(f"Warning: Could not fetch cloud templates: {err}")
