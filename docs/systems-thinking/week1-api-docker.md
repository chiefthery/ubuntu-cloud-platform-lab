
## Goals

- Package a minimal FastAPI service into a reproducible container image.
- Run the service on Ubuntu (EC2) using Docker.
- Enforce least-privilege by running as a non-root user.
- Stream logs to stdout/stderr for platform-native observability.
- Add container-native health checks.
- Validate the container under read-only filesystem constraints.

---

## Architecture

### Host (EC2 Ubuntu)

- Runs Docker Engine + Docker Compose
- Publishes port **8000** to the outside world (or at least host network)

### Container (platform-api)

- Base image: python:3.12-slim

- Dedicated service user: `app` (UID/GID 10001)

- Runs `uvicorn` serving FastAPI on 0.0.0.0:8000

- Exposes `/health` endpoint for verification

- Logs to stdout

### Security Posture

#### Non-root execution
    
The container creates and runs as a dedicated service user:

```
RUN groupadd --gid 10001 app && \
    useradd --uid 10001 --gid 10001 --create-home --shell /usr/sbin/nologin app

USER app
```

Why:
- Prevents root execution inside the container
- Reduces blast radius in case of compromise
- Aligns with least-privilege principles used in Linux system hardening

Verified via:

```
docker exec <container> whoami
# app

docker exec <container> id
# uid=10001(app)
```

### Read-only filesystem validation

Container tested with:

`docker run --read-only --tmpfs /tmp -p 8000:8000 ubuntu-lab-app:nonroot`

Why:

- Ensures application does not rely on writable container filesystem

- Forces ephemeral writes into `/tmp`

- Mimics hardened runtime environments (ECS/Kubernetes)

Result:

- Service continued functioning normally

- Health endpoint returned `200 OK`

---

## Key Decisions

### Pinned dependencies

- in `requirements.txt` for reproducibility (avoid “works on my machine” drift).

### Layer-caching build

-  copy/install requirements before copying app code to speed rebuilds.

### Bind to `0.0.0.0` 

- inside container so Docker port-mapping works (binding to `127.0.0.1` would break external access).

### Container-native HEALTHCHECK

```
HEALTHCHECK --interval=10s --timeout=3s --start-period=10s --retries=3 \
  CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=2)"]
```

- Enables Docker (and future ECS/K8s) to determine container health
- Establishes contract for orchestration layer

### Logs to stdout

- Avoids writing local log files

- Allows `docker logs` / Compose / CloudWatch capture

---

## Verification

- **Service is running:**

    - `docker ps` shows container up with `0.0.0.0:8000->8000/tcp`

- **API responds:**

    - `curl -s http://localhost:8000/health` returns `{"status":"ok"}`

- **Healthcheck operational:**

    - `docker inspect --format='{{json .State.Health}}' <container>` shows `"Status": "healthy"`

- **Process ownership:**

```
docker exec <container> whoami
# app
```
