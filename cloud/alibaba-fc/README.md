# Alibaba Cloud Function Compute

**Files:** `Dockerfile`, `handler.py`, `s.yaml`

## Prerequisites

- Alibaba Cloud CLI configured (`aliyun configure`)
- [Serverless Devs](https://www.serverless-devs.com/) (`npm install -g @serverless-devs/s`)
- Docker
- ACR (Alibaba Container Registry) namespace created

## Setup

```bash
# Configure Serverless Devs credentials (first time only)
s config add --AccessKeyID <your-access-key-id> --AccessKeySecret <your-access-key-secret> -a default

# Create ACR namespace (first time only)
aliyun cr CreateNamespace --Namespace <namespace>
```

## Deploy

```bash
# Build and push the Docker image
docker build -t registry.<region>.aliyuncs.com/<namespace>/<project_name>:latest .
docker push registry.<region>.aliyuncs.com/<namespace>/<project_name>:latest

# Deploy the function
s deploy
```

## Invoke

```bash
s invoke
```

## View logs

```bash
s logs --tail
```

## Important

- Do not rename `handler.py` or the `handler()` function — `s.yaml` references `handler.handler`
- Do not rename `workflow.py` or the `main()` function — `handler.py` imports it
- The `s.yaml` has the function name, region, and container image pre-configured from cookiecutter
- To add triggers (HTTP, timer, OSS, etc.), edit the `triggers` section in `s.yaml`
