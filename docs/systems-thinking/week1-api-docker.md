# Week 1: Docker + API

## Goals

- Package a minimal API into a reproducible container image.
- Run it locally on the EC2 host using Compose with predictable networking.
- Ensure logs stream to stdout/stderr so the platform (Docker/Compose) can capture them.
- Establish a baseline “service-like” lifecycle: build → run → restart → observe.

---

## Architecture

- **Host (EC2 Ubuntu):**

    - Runs Docker Engine + Docker Compose

    - Publishes port **8000** to the outside world (or at least host network)

- **Compose project network (`platform-api_default`):**

    - Private bridge network created by Compose for service isolation + DNS

- **Container (`api` service):**

    - Runs `uvicorn` serving FastAPI on `0.0.0.0:8000`

    - App endpoint `/health` used for functional verification

- **Observability (basic):**

    - App logs to stdout → captured by `docker compose logs`

---

## Key Decisions

- **Pinned dependencies** in `requirements.txt` for reproducibility (avoid “works on my machine” drift).

- **Layer-caching build:** copy/install requirements before copying app code to speed rebuilds.

- **Bind to** `0.0.0.0` inside container so Docker port-mapping works (binding to `127.0.0.1` would break external access).

- **Compose restart policy** (`unless-stopped`) to mimic systemd-like resilience.

- **Log to stdout** so containers can be treated as managed processes (instead of writing local log files inside the container).

---

## Verification

- **Service is running:**

    - `docker ps` shows container up with `0.0.0.0:8000->8000/tcp`

- **API responds:**

    - `curl -s http://localhost:8000/health` returns `{"status":"ok"}`

- **Logs are observable:**

    - `docker compose logs --tail=50` shows uvicorn startup + health request + app log line
