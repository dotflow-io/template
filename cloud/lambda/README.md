# AWS Lambda

**Files:** `Dockerfile`, `handler.py`, `template.yaml`, `samconfig.toml`

## Prerequisites

- AWS CLI configured (`aws configure`)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) (`brew install aws-sam-cli`)
- Docker

## Deploy

```bash
sam build
sam deploy
```

That's it. SAM builds the Docker image, pushes to ECR, and creates the Lambda function.

## Invoke

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
- The `samconfig.toml` has the stack name, region, and ECR repository pre-configured from cookiecutter
- To change the schedule or add triggers, edit `template.yaml` (see `lambda-scheduled` template)
