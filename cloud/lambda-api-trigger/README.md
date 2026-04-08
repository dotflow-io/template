# AWS Lambda + API Gateway

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

The `template.yaml` includes an API Gateway HTTP POST endpoint that triggers the Lambda.

## Invoke manually

```bash
# Via SAM
sam remote invoke

# Via API Gateway (after deploy, check the output URL)
curl -X POST <api_gateway_url>
```

## View logs

```bash
sam logs --stack-name <project_name> --tail
```

## Important

- Do not rename `handler.py` or the `handler()` function — the `Dockerfile` CMD is `handler.handler`
- Do not rename `workflow.py` or the `main()` function — `handler.py` imports it
- The API Gateway URL is shown in the CloudFormation outputs after deploy
- The `samconfig.toml` has stack name, region, and ECR repository pre-configured
