# dotflow template

This repository is a **Cookiecutter template** for generating a **dotflow** workflow project, with optional **cloud deployment scaffolding**.

## Prerequisites

- Python **>= 3.9**
- `cookiecutter` installed (via `pipx` or `pip`)

## Generate a project

```bash
cookiecutter https://github.com/dotflow-io/template.git
```

You'll be prompted for these options:

| Option | Description |
|------|-----------|
| `project_name` | Generated project name (e.g. `my_pipeline`) |
| `module_name` | Python module name (derived from `project_name`, with `-` replaced by `_`) |
| `storage` | Storage backend (`default`, `file`, `s3`, `gcs`) |
| `scheduler` | Scheduling (`none`, `cron`) |
| `execution_mode` | Execution (`sequential`, `parallel`, `background`) |
| `retry` | Enable retry (`no`, `yes`) |
| `checkpoint` | Enable checkpointing (`no`, `yes`) |
| `cloud` | Adds deployment files (`none`, `docker`, `lambda`, `lambda-scheduled`, `lambda-s3-trigger`, `lambda-sqs-trigger`, `lambda-api-trigger`, `ecs`, `ecs-scheduled`, `cloud-run`, `cloud-run-scheduled`, `kubernetes`) |
| `schedule_expression` | Cron or rate expression for scheduled platforms (e.g. `rate(6 hours)`, `cron(0 12 * * ? *)`) |

## Cloud templates

When the `cloud` option is set to a value other than `none`, the post-generation hook copies the corresponding infrastructure files (e.g. `Dockerfile`, `docker-compose.yml`, `handler.py`) into the generated project root.

You can also generate cloud files separately using the CLI:

```bash
dotflow cloud generate --platform lambda
dotflow cloud list
```

### Available platforms

| Value | Icon | Platform | Available | Deploy guide |
|---|---|---|---|---|
| `none` | 🚫 | — | — | — |
| `docker` | <img alt="Docker" src="https://cdn.simpleicons.org/docker" width="18" /> | Docker | :white_check_mark: | [Deploy](cloud/docker/README.md) |
| `lambda` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> | AWS Lambda | :white_check_mark: | [Deploy](cloud/lambda/README.md) |
| `lambda-scheduled` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon EventBridge" src="https://api.iconify.design/logos:aws-eventbridge.svg" width="18" /> | AWS Lambda + EventBridge Schedule | :white_check_mark: | [Deploy](cloud/lambda-scheduled/README.md) |
| `lambda-s3-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon S3" src="https://api.iconify.design/logos:aws-s3.svg" width="18" /> | AWS Lambda + S3 Trigger | :white_check_mark: | [Deploy](cloud/lambda-s3-trigger/README.md) |
| `lambda-sqs-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon SQS" src="https://api.iconify.design/logos:aws-sqs.svg" width="18" /> | AWS Lambda + SQS Trigger | :white_check_mark: | [Deploy](cloud/lambda-sqs-trigger/README.md) |
| `lambda-api-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon API Gateway" src="https://api.iconify.design/logos:aws-api-gateway.svg" width="18" /> | AWS Lambda + API Gateway | :white_check_mark: | [Deploy](cloud/lambda-api-trigger/README.md) |
| `ecs` | <img alt="Amazon ECS" src="https://www.vectorlogo.zone/logos/amazon_ecs/amazon_ecs-icon.svg" width="18" /> | AWS ECS (Fargate) | :white_check_mark: | [Deploy](cloud/ecs/README.md) |
| `ecs-scheduled` | <img alt="Amazon ECS" src="https://www.vectorlogo.zone/logos/amazon_ecs/amazon_ecs-icon.svg" width="18" /> <img alt="Amazon EventBridge" src="https://api.iconify.design/logos:aws-eventbridge.svg" width="18" /> | AWS ECS + EventBridge Schedule | :white_check_mark: | [Deploy](cloud/ecs-scheduled/README.md) |
| `cloud-run` | <img alt="Google Cloud" src="https://cdn.simpleicons.org/googlecloud" width="18" /> | Google Cloud Run | :white_check_mark: | [Deploy](cloud/cloud-run/README.md) |
| `cloud-run-scheduled` | <img alt="Google Cloud Run" src="https://cdn.simpleicons.org/googlecloud" width="18" /> <img alt="Cloud Scheduler" src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" width="18" /> | Cloud Run + Cloud Scheduler | :white_check_mark: | [Deploy](cloud/cloud-run-scheduled/README.md) |
| `kubernetes` | <img alt="Kubernetes" src="https://cdn.simpleicons.org/kubernetes" width="18" /> | Kubernetes | :white_check_mark: | [Deploy](cloud/kubernetes/README.md) |
| `azure-functions` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Functions | :soon: | — |
| `azure-container` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Container Apps | :soon: | — |
| `heroku` | <img alt="Heroku" src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" width="18" /> | Heroku | :soon: | — |
| `fly-io` | <img alt="Fly.io" src="https://cdn.simpleicons.org/flydotio" width="18" /> | Fly.io | :soon: | — |
| `railway` | <img alt="Railway" src="https://cdn.simpleicons.org/railway" width="18" /> | Railway | :soon: | — |
| `render` | <img alt="Render" src="https://cdn.simpleicons.org/render" width="18" /> | Render | :soon: | — |
| `digital-ocean` | <img alt="DigitalOcean" src="https://cdn.simpleicons.org/digitalocean" width="18" /> | DigitalOcean App Platform | :soon: | — |

## Next steps (inside the generated project)

Run locally without Docker:

```bash
pip install -e ".[dev]"
python -m <your_module_name>.workflow
```

Run tests:

```bash
pytest
```

## Template structure

- `cookiecutter.json`: defines the prompt questions/options.
- `{{cookiecutter.project_name}}/`: generated Python project skeleton.
- `hooks/post_gen_project.py`: hook that downloads `cloud/` files based on the selected `cloud` option.
- `cloud/`: catalog of platforms and available files (see `cloud/registry.json`).
