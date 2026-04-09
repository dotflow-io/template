# Dotflow Template

Official project template for [dotflow](https://github.com/dotflow-io/dotflow) — the lightweight Python library for execution pipelines.

## Cloud deployment

Deploy your dotflow pipelines to any major cloud provider. Choose a target platform during project creation and get all the infrastructure files you need — fully configured and ready to deploy.

## CLI

| Command | Description |
|---------|-------------|
| `dotflow init` | Scaffold a new project (interactive) |
| `dotflow cloud list` | Show available deployment platforms |
| `dotflow cloud generate --platform <name>` | Generate deployment files for an existing project |
| `dotflow deploy --platform <name> --project <name>` | Deploy to AWS, GCP, Alibaba, GitHub |

---

### Available platforms

| Value | Icon | Platform | Deploy method | Guide |
|---|---|---|---|---|
| `none` | 🚫 | — | — | — |
| `docker` | <img alt="Docker" src="https://cdn.simpleicons.org/docker" width="18" /> | Docker | `docker compose up` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/docker/) |
| `lambda` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> | AWS Lambda | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/lambda/) |
| `lambda-scheduled` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon EventBridge" src="https://api.iconify.design/logos:aws-eventbridge.svg" width="18" /> | AWS Lambda + EventBridge | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/lambda-scheduled/) |
| `lambda-s3-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon S3" src="https://api.iconify.design/logos:aws-s3.svg" width="18" /> | AWS Lambda + S3 Trigger | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/lambda-s3-trigger/) |
| `lambda-sqs-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon SQS" src="https://api.iconify.design/logos:aws-sqs.svg" width="18" /> | AWS Lambda + SQS Trigger | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/lambda-sqs-trigger/) |
| `lambda-api-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon API Gateway" src="https://api.iconify.design/logos:aws-api-gateway.svg" width="18" /> | AWS Lambda + API Gateway | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/lambda-api-trigger/) |
| `ecs` | <img alt="Amazon ECS" src="https://www.vectorlogo.zone/logos/amazon_ecs/amazon_ecs-icon.svg" width="18" /> | AWS ECS (Fargate) | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/ecs/) |
| `ecs-scheduled` | <img alt="Amazon ECS" src="https://www.vectorlogo.zone/logos/amazon_ecs/amazon_ecs-icon.svg" width="18" /> <img alt="Amazon EventBridge" src="https://api.iconify.design/logos:aws-eventbridge.svg" width="18" /> | AWS ECS + EventBridge | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/ecs-scheduled/) |
| `cloud-run` | <img alt="Google Cloud" src="https://cdn.simpleicons.org/googlecloud" width="18" /> | Google Cloud Run | `gcloud run deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/cloud-run/) |
| `cloud-run-scheduled` | <img alt="Google Cloud Run" src="https://cdn.simpleicons.org/googlecloud" width="18" /> <img alt="Cloud Scheduler" src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" width="18" /> | Cloud Run + Scheduler | `gcloud` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/cloud-run-scheduled/) |
| `kubernetes` | <img alt="Kubernetes" src="https://cdn.simpleicons.org/kubernetes" width="18" /> | Kubernetes | `kubectl apply` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/kubernetes/) |
| `azure-functions` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Functions | :soon: | — |
| `azure-container` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Container Apps | :soon: | — |
| `heroku` | <img alt="Heroku" src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" width="18" /> | Heroku | :soon: | — |
| `fly-io` | <img alt="Fly.io" src="https://cdn.simpleicons.org/flydotio" width="18" /> | Fly.io | :soon: | — |
| `railway` | <img alt="Railway" src="https://cdn.simpleicons.org/railway" width="18" /> | Railway | :soon: | — |
| `render` | <img alt="Render" src="https://cdn.simpleicons.org/render" width="18" /> | Render | :soon: | — |
| `digital-ocean` | <img alt="DigitalOcean" src="https://cdn.simpleicons.org/digitalocean" width="18" /> | DigitalOcean App Platform | :soon: | — |
| `step-functions` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> | AWS Step Functions | :soon: | — |
| `aws-batch` | <img alt="AWS" src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-icon.svg" width="18" /> | AWS Batch | :soon: | — |
| `app-runner` | <img alt="AWS" src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-icon.svg" width="18" /> | AWS App Runner | :soon: | — |
| `cloud-functions` | <img alt="Google Cloud" src="https://cdn.simpleicons.org/googlecloud" width="18" /> | Google Cloud Functions | :soon: | — |
| `cloud-workflows` | <img alt="Google Cloud" src="https://cdn.simpleicons.org/googlecloud" width="18" /> | Google Cloud Workflows | :soon: | — |
| `cloud-tasks` | <img alt="Google Cloud" src="https://cdn.simpleicons.org/googlecloud" width="18" /> | Google Cloud Tasks | :soon: | — |
| `pubsub-trigger` | <img alt="Google Cloud" src="https://cdn.simpleicons.org/googlecloud" width="18" /> | Google Pub/Sub Trigger | :soon: | — |
| `azure-container-instances` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Container Instances | :soon: | — |
| `azure-logic-apps` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Logic Apps | :soon: | — |
| `azure-queue-trigger` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Functions + Queue Trigger | :soon: | — |
| `github-actions` | <img alt="GitHub Actions" src="https://cdn.simpleicons.org/githubactions" width="18" /> | GitHub Actions | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/github-actions/) |
| `gitlab-ci` | <img alt="GitLab" src="https://cdn.simpleicons.org/gitlab" width="18" /> | GitLab CI | :soon: | — |
| `vercel` | <img alt="Vercel" src="https://cdn.simpleicons.org/vercel" width="18" /> | Vercel | :soon: | — |
| `coolify` | <img alt="Coolify" src="https://cdn.simpleicons.org/coolify" width="18" /> | Coolify | :soon: | — |
| `nomad` | <img alt="HashiCorp" src="https://cdn.simpleicons.org/hashicorp" width="18" /> | HashiCorp Nomad | :soon: | — |
| `terraform` | <img alt="Terraform" src="https://cdn.simpleicons.org/terraform" width="18" /> | Terraform | :soon: | — |
| `linode` | <img alt="Linode" src="https://api.iconify.design/logos:linode.svg" width="18" /> | Linode (Akamai) | :soon: | — |
| `vultr` | <img alt="Vultr" src="https://cdn.simpleicons.org/vultr" width="18" /> | Vultr | :soon: | — |
| `oracle-cloud` | <img alt="Oracle" src="https://api.iconify.design/logos:oracle.svg" width="18" /> | Oracle Cloud | :soon: | — |
| `civo` | <img alt="Civo" src="https://cdn.simpleicons.org/civo" width="18" /> | Civo | :soon: | — |
| `proxmox` | <img alt="Proxmox" src="https://cdn.simpleicons.org/proxmox" width="18" /> | Proxmox | :soon: | — |
| `k3s` | <img alt="K3s" src="https://cdn.simpleicons.org/k3s" width="18" /> | K3s | :soon: | — |
| `alibaba-fc` | <img alt="Alibaba Cloud" src="https://cdn.simpleicons.org/alibabacloud" width="18" /> | Alibaba Cloud Function Compute | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/alibaba-fc/) |
| `alibaba-fc-scheduled` | <img alt="Alibaba Cloud" src="https://cdn.simpleicons.org/alibabacloud" width="18" /> <img alt="Alibaba Cloud" src="https://cdn.simpleicons.org/alibabacloud" width="18" /> | Alibaba Cloud FC + Timer Trigger | `dotflow deploy` | [Guide](https://dotflow-io.github.io/dotflow/nav/cloud/alibaba-fc-scheduled/) |
