# Google Cloud Run + Cloud Scheduler

**Files:** `Dockerfile`, `cloudbuild.yaml`, `scheduler.yaml`

## Prerequisites

- Google Cloud CLI (`gcloud`) installed and authenticated

## Deploy

```bash
gcloud auth login
gcloud config set project <gcp_project_id>

# Enable APIs
gcloud services enable cloudbuild.googleapis.com run.googleapis.com cloudscheduler.googleapis.com

# Deploy Cloud Run service
gcloud run deploy <project_name> --source . --region us-central1 --no-allow-unauthenticated

# Create Cloud Scheduler job (adjust the URL from the deploy output)
gcloud scheduler jobs create http <project_name>-trigger \
  --schedule="0 */6 * * *" \
  --uri="<cloud_run_url>" \
  --http-method=POST \
  --oidc-service-account-email=<project_number>-compute@developer.gserviceaccount.com \
  --location=us-central1
```

## View logs

```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=<project_name>" --limit 50 --format="value(textPayload)"
```

## Important

- Do not rename `workflow.py` or the `main()` function — the `Dockerfile` CMD depends on it
- The `cloudbuild.yaml` references `gcp_project_id` and `gcp_region` — these must match your GCP project
- Replace `<cloud_run_url>` with the actual URL from the `gcloud run deploy` output
- The scheduler uses OIDC authentication to invoke the Cloud Run service
