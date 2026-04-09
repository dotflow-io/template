# Alibaba Cloud Function Compute + Timer Trigger

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

# Deploy the function with timer trigger
s deploy
```

## Invoke manually

```bash
s invoke
```

## View logs

```bash
s logs --tail
```

## Schedule syntax

The timer trigger uses **cron expressions** (China Standard Time — UTC+8):

| Expression | Meaning |
|---|---|
| `0 */6 * * *` | Every 6 hours |
| `0 0 * * *` | Daily at midnight |
| `0 9 * * 1` | Every Monday at 9:00 AM |
| `*/5 * * * *` | Every 5 minutes |

## Important

- Do not rename `handler.py` or the `handler()` function — `s.yaml` references `handler.handler`
- Do not rename `workflow.py` or the `main()` function — `handler.py` imports it
- The `s.yaml` has the function name, region, container image, and schedule pre-configured from cookiecutter
- Timer triggers use China Standard Time (CST/UTC+8) by default
- To change the schedule after deploy, edit `cronExpression` in `s.yaml` and run `s deploy` again
