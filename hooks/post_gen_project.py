"""Post-generation hook: fetch cloud templates for the selected platform."""

import json
from pathlib import Path
from urllib.request import urlopen

CLOUD_URL = (
    "https://raw.githubusercontent.com/dotflow-io/templates/master/cloud"
)

CLOUD = "{{ cookiecutter.cloud }}"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"

BOLD = "\033[1m"
CYAN = "\033[36m"
RESET = "\033[0m"


def prompt(label: str, default: str = "") -> str:
    if default:
        value = input(
            f"    {BOLD}{label}{RESET} ({CYAN}{default}{RESET}): "
        ).strip()
        return value or default
    return input(f"    {BOLD}{label}{RESET}: ").strip()


def ask_inputs() -> dict:
    sanitized_name = PROJECT_NAME.replace("_", "-").lower()
    placeholders = {
        "PROJECT_NAME": sanitized_name,
        "MODULE_NAME": MODULE_NAME,
        "STACK_NAME": sanitized_name,
        "K8S_NAME": sanitized_name,
    }

    if CLOUD in {
        "lambda-scheduled", "ecs-scheduled",
        "cloud-run-scheduled", "github-actions",
        "alibaba-fc-scheduled",
    }:
        cron = prompt("cron_expression", "0 */6 * * *")
        placeholders["SCHEDULE_EXPRESSION"] = (
            _crontab_to_aws(cron)
            if CLOUD in {
                "lambda-scheduled",
                "ecs-scheduled",
            }
            else cron
        )

    if CLOUD in {
        "lambda", "lambda-scheduled", "lambda-s3-trigger",
        "lambda-sqs-trigger", "lambda-api-trigger",
        "ecs", "ecs-scheduled",
    }:
        placeholders["AWS_ACCOUNT_ID"] = prompt("aws_account_id")
        placeholders["AWS_REGION"] = prompt("aws_region", "us-east-1")

    if CLOUD in {"cloud-run", "cloud-run-scheduled"}:
        placeholders["GCP_PROJECT_ID"] = prompt("gcp_project_id")
        placeholders["GCP_REGION"] = prompt("gcp_region", "us-central1")

    if CLOUD in {"alibaba-fc", "alibaba-fc-scheduled"}:
        placeholders["ALIBABA_NAMESPACE"] = prompt("alibaba_namespace")
        placeholders["ALIBABA_REGION"] = prompt("alibaba_region", "cn-hangzhou")
        placeholders["ALIBABA_CR_PASSWORD"] = prompt("alibaba_cr_password")

    return placeholders


def fetch_registry() -> dict:
    content = urlopen(f"{CLOUD_URL}/registry.json", timeout=10).read()
    return json.loads(content)


def fetch_file(platform: str, filename: str) -> str:
    url = f"{CLOUD_URL}/{platform}/{filename}"
    return urlopen(url, timeout=10).read().decode()


def _crontab_to_aws(expression: str) -> str:
    """Convert 5-field crontab to AWS EventBridge cron."""
    parts = expression.strip().split()
    if len(parts) != 5:
        return expression
    minute, hour, dom, month, dow = parts
    if dow != "*" and dom == "*":
        dom = "?"
    else:
        dow = "?"
    return f"cron({minute} {hour} {dom} {month} {dow} *)"


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
        try:
            content = fetch_file(CLOUD, filename)
        except Exception as err:
            print(f"  Warning: Failed to fetch {filename}: {err}")
            continue

        content = replace_placeholders(content, placeholders)

        try:
            filepath = project_dir / filename
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content)
        except OSError as err:
            print(f"  Warning: Failed to write {filename}: {err}")

    generate_env_file(project_dir, placeholders)


def generate_env_file(project_dir: Path, placeholders: dict):
    """Generate .env file with cloud credentials."""
    env_vars = {}

    if CLOUD in {
        "lambda", "lambda-scheduled", "lambda-s3-trigger",
        "lambda-sqs-trigger", "lambda-api-trigger",
        "ecs", "ecs-scheduled",
    }:
        env_vars["AWS_DEFAULT_REGION"] = placeholders.get("AWS_REGION", "us-east-1")

    if CLOUD in {"cloud-run", "cloud-run-scheduled"}:
        env_vars["GCP_PROJECT_ID"] = placeholders.get("GCP_PROJECT_ID", "")
        env_vars["GCP_REGION"] = placeholders.get("GCP_REGION", "us-central1")

    if CLOUD in {"alibaba-fc", "alibaba-fc-scheduled"}:
        env_vars["ALIBABA_CR_PASSWORD"] = placeholders.get("ALIBABA_CR_PASSWORD", "")
        env_vars["ALIBABA_CLOUD_REGION"] = placeholders.get("ALIBABA_REGION", "cn-hangzhou")

    if not env_vars:
        return

    env_path = project_dir / ".env"
    lines = [f"{k}={v}" for k, v in env_vars.items()]
    env_path.write_text("\n".join(lines) + "\n")
    print(f"  Created: {env_path}")


try:
    generate_cloud_files()
except KeyboardInterrupt:
    print("\nAborted.")
except Exception as err:
    print(f"Warning: Could not generate cloud templates: {err}")
