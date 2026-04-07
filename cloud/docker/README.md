# Docker

**Files:** `Dockerfile`, `docker-compose.yml`

## Prerequisites

- Docker

## Deploy

```bash
docker compose build
docker compose up
```

## Important

- Do not rename the `workflow.py` module or the `main()` function — the `Dockerfile` CMD depends on it
- The `docker-compose.yml` uses the `project_name` as container name
