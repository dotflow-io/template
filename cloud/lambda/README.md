# AWS Lambda

**Files:** `Dockerfile`, `handler.py`

## Prerequisites

- AWS CLI configured (`aws configure`)
- Docker

## Deploy

```bash
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=us-east-1

# Login to ECR
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

# Create repository
aws ecr create-repository --repository-name <project_name> --region $REGION

# Build and push
docker build -t <project_name> .
docker tag <project_name>:latest $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/<project_name>:latest
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/<project_name>:latest

# Create Lambda function
aws lambda create-function \
  --function-name <project_name> \
  --package-type Image \
  --code ImageUri=$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/<project_name>:latest \
  --role arn:aws:iam::$ACCOUNT_ID:role/lambda-execution-role \
  --region $REGION

# Invoke
aws lambda invoke --function-name <project_name> --region $REGION /dev/stdout
```
