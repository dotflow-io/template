# AWS Lambda + S3 Trigger

**Files:** `Dockerfile`, `handler.py`, `template.yaml`, `samconfig.toml`

## Prerequisites

- AWS CLI configured (`aws configure`)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) (`brew install aws-sam-cli`)
- Docker

## Deploy

### Option 1: dotflow deploy

```bash
dotflow deploy --platform lambda-s3-trigger --project <project_name>
```

### Option 2: SAM CLI

```bash
aws ecr create-repository --repository-name <project_name> --region us-east-1
sam build
sam deploy
```

The `template.yaml` includes an S3 event that triggers the Lambda when a file is uploaded to the configured bucket.

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
- Edit the S3 bucket name and prefix in `template.yaml` before deploying
- The `samconfig.toml` has stack name, region, and ECR repository pre-configured
