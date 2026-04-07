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
| `cloud` | Adds deployment files (`none`, `docker`, `lambda`, `ecs`) |

## Cloud templates

When the `cloud` option is set to a value other than `none`, the post-generation hook copies the corresponding infrastructure files (e.g. `Dockerfile`, `docker-compose.yml`, `handler.py`) into the generated project root.

You can also generate cloud files separately using the CLI:

```bash
dotflow cloud generate --platform lambda
dotflow cloud list
```

### Available platforms

| `cloud` value | Logo | Platform | Available | Notes |
|---|---|---|---|---|
| `none` | 🚫 | — | — | No deployment files |
| `docker` | <img alt="Docker" src="https://cdn.simpleicons.org/docker" width="18" /> | Docker | :white_check_mark: | `Dockerfile` and `docker-compose.yml` |
| `lambda` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> | AWS Lambda | :white_check_mark: | Container-based Lambda handler template |
| `ecs` | <img alt="Amazon ECS" src="https://www.vectorlogo.zone/logos/amazon_ecs/amazon_ecs-icon.svg" width="18" /> | AWS ECS (Fargate) | :white_check_mark: | Task definition template (often paired with Amazon ECR) |
| `cloud-run` | <img alt="Google Cloud" src="https://cdn.simpleicons.org/googlecloud" width="18" /> | Google Cloud Run | :soon: | Includes `cloudbuild.yaml` |
| `kubernetes` | <img alt="Kubernetes" src="https://cdn.simpleicons.org/kubernetes" width="18" /> | Kubernetes | :soon: | Deployment + service manifests |
| `azure-functions` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Functions | :soon: | `function.json` + `host.json` |
| `azure-container` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Container Apps | :soon: | `container-app.yaml` |
| `heroku` | <img alt="Heroku" src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" width="18" /> | Heroku | :soon: | `Procfile` + `heroku.yml` |
| `fly-io` | <img alt="Fly.io" src="https://cdn.simpleicons.org/flydotio" width="18" /> | Fly.io | :soon: | `fly.toml` |
| `railway` | <img alt="Railway" src="https://cdn.simpleicons.org/railway" width="18" /> | Railway | :soon: | `railway.json` |
| `render` | <img alt="Render" src="https://cdn.simpleicons.org/render" width="18" /> | Render | :soon: | `render.yaml` |
| `digital-ocean` | <img alt="DigitalOcean" src="https://cdn.simpleicons.org/digitalocean" width="18" /> | DigitalOcean App Platform | :soon: | `app.yaml` |

## Next steps (inside the generated project)

Enter the generated folder and run:

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
