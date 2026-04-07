# AWS ECS + EventBridge Schedule

**Files:** `Dockerfile`, `template.yaml`

## Prerequisites

- AWS CLI configured (`aws configure`)
- Docker

## Deploy

```bash
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=us-east-1

# Login to ECR
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

# Create repository, build and push
aws ecr create-repository --repository-name <project_name> --region $REGION
docker build -t <project_name> .
docker tag <project_name>:latest $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/<project_name>:latest
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/<project_name>:latest

# Deploy CloudFormation stack
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name <project_name> \
  --capabilities CAPABILITY_IAM \
  --region $REGION
```

## View logs

```bash
aws logs get-log-events --log-group-name /ecs/<project_name> \
  --log-stream-name $(aws logs describe-log-streams --log-group-name /ecs/<project_name> --order-by LastEventTime --descending --query "logStreams[0].logStreamName" --output text --region $REGION) \
  --region $REGION --query "events[].message" --output text
```

## Important

- Do not rename `workflow.py` or the `main()` function — the `Dockerfile` CMD depends on it
- The schedule expression in `template.yaml` uses AWS EventBridge syntax
- Edit `aws_account_id` and `aws_region` in `template.yaml` before deploying
- The ECS task runs on Fargate and stops after the workflow completes
