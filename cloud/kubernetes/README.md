# Kubernetes

**Files:** `Dockerfile`, `deployment.yaml`, `service.yaml`

## Prerequisites

- Docker
- `kubectl`
- A Kubernetes cluster (minikube for local testing)

## Local deploy (minikube)

```bash
# Install minikube (macOS)
brew install minikube

# Start cluster and use its Docker daemon
minikube start
eval $(minikube docker-env)

# Build inside minikube
docker build -t <project_name>:latest .

# Deploy
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Check status
kubectl get pods -l app=<project_name>

# View logs
kubectl logs -l app=<project_name>
```

## Production deploy

Replace `image: <project_name>:latest` in `deployment.yaml` with your container registry URL, then:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
