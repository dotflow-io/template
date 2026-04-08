# AWS Lambda + SQS Trigger

**Files:** `Dockerfile`, `handler.py`, `template.yaml`, `samconfig.toml`

## Prerequisites

- AWS CLI configured (`aws configure`)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) (`brew install aws-sam-cli`)
- Docker

## Deploy

```bash
# Create ECR repository (first time only)
aws ecr create-repository --repository-name <project_name> --region us-east-1

sam build
sam deploy
```

The `template.yaml` includes an SQS event source that triggers the Lambda when messages arrive in the queue.

## Invoke manually

```bash
sam remote invoke
```

## View logs

```bash
sam logs --stack-name <project_name> --tail
```

## Important

- Do not rename `handler.py` or the `handler()` function — the `Dockerfile` CMD is `handler.handler`
- Do not rename `workflow.py` or the `main()` function — `handler.py` imports it
- The SQS queue is created by the SAM template — check `template.yaml` for queue configuration
- The `samconfig.toml` has stack name, region, and ECR repository pre-configured
