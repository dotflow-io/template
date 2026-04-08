"""Post-generation hook: fetch cloud templates for the selected platform."""

import json
from pathlib import Path
from urllib.request import urlopen

CLOUD_URL = "https://raw.githubusercontent.com/dotflow-io/template/master/cloud"

CLOUD = "{{ cookiecutter.cloud }}"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"

AWS_PLATFORMS = {
    "lambda", "lambda-scheduled", "lambda-s3-trigger",
    "lambda-sqs-trigger", "lambda-api-trigger", "ecs", "ecs-scheduled",
}
GCP_PLATFORMS = {"cloud-run", "cloud-run-scheduled"}
SCHEDULED_PLATFORMS = {"lambda-scheduled", "ecs-scheduled", "cloud-run-scheduled"}


def ask_inputs() -> dict:
    placeholders = {
        "PROJECT_NAME": PROJECT_NAME,
        "MODULE_NAME": MODULE_NAME,
        "STACK_NAME": PROJECT_NAME.replace("_", "-"),
        "K8S_NAME": PROJECT_NAME.replace("_", "-"),
    }

    if CLOUD in SCHEDULED_PLATFORMS:
        placeholders["SCHEDULE_EXPRESSION"] = (
            input("Schedule expression [rate(6 hours)]: ").strip()
            or "rate(6 hours)"
        )

    if CLOUD in AWS_PLATFORMS:
        placeholders["AWS_ACCOUNT_ID"] = input("AWS Account ID: ").strip()
        placeholders["AWS_REGION"] = (
            input("AWS Region [us-east-1]: ").strip() or "us-east-1"
        )

    if CLOUD in GCP_PLATFORMS:
        placeholders["GCP_PROJECT_ID"] = input("GCP Project ID: ").strip()
        placeholders["GCP_REGION"] = (
            input("GCP Region [us-central1]: ").strip() or "us-central1"
        )

    return placeholders


def fetch_registry() -> dict:
    content = urlopen(f"{CLOUD_URL}/registry.json", timeout=10).read()
    return json.loads(content)


def fetch_file(platform: str, filename: str) -> str:
    url = f"{CLOUD_URL}/{platform}/{filename}"
    return urlopen(url, timeout=10).read().decode()


def replace_placeholders(content: str, placeholders: dict) -> str:
    for key, value in placeholders.items():
        tag = "{" + "{" + key + "}" + "}"
        content = content.replace(tag, value)
    return content


def generate_cloud_files():
    if CLOUD == "none":
        return

    placeholders = ask_inputs()

    registry = fetch_registry()
    platform = registry["platforms"].get(CLOUD)
    if not platform:
        return

    project_dir = Path.cwd()

    for filename in platform["files"]:
        content = fetch_file(CLOUD, filename)
        content = replace_placeholders(content, placeholders)
        (project_dir / filename).write_text(content)


try:
    generate_cloud_files()
except Exception as err:
    print(f"Warning: Could not fetch cloud templates: {err}")
