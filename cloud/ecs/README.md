# AWS ECS (Fargate)

**Files:** `Dockerfile`, `task-definition.json`

## Prerequisites

- AWS CLI configured (`aws configure`)
- Docker

## Deploy

```bash
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=us-east-1

# Create execution role (first time only)
aws iam create-role --role-name ecsTaskExecutionRole \
  --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"ecs-tasks.amazonaws.com"},"Action":"sts:AssumeRole"}]}'
aws iam attach-role-policy --role-name ecsTaskExecutionRole \
  --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy

# Login to ECR
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

# Create repository, build and push
aws ecr create-repository --repository-name <project_name> --region $REGION
docker build -t <project_name> .
docker tag <project_name>:latest $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/<project_name>:latest
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/<project_name>:latest

# Create log group
aws logs create-log-group --log-group-name /ecs/<project_name> --region $REGION

# Register task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json --region $REGION

# Create cluster
aws ecs create-cluster --cluster-name dotflow --region $REGION

# Run task
SUBNET=$(aws ec2 describe-subnets --query "Subnets[0].SubnetId" --output text --region $REGION)
aws ecs run-task --cluster dotflow --task-definition <project_name> --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[$SUBNET],assignPublicIp=ENABLED}" --region $REGION
```

## View logs

```bash
aws logs get-log-events --log-group-name /ecs/<project_name> \
  --log-stream-name $(aws logs describe-log-streams --log-group-name /ecs/<project_name> --order-by LastEventTime --descending --query "logStreams[0].logStreamName" --output text --region $REGION) \
  --region $REGION --query "events[].message" --output text
```

## Important

- Do not rename `workflow.py` or the `main()` function — the `Dockerfile` CMD depends on it
- The `task-definition.json` references the ECR image URI, `executionRoleArn`, and CloudWatch log group — do not change these unless you also update the corresponding AWS resources
- The `aws_account_id` and `aws_region` must match your actual AWS account and region
- Create the CloudWatch log group before running the task, otherwise the container will fail to start
