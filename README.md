
# Ubuntu Cloud Platform Lab

Production-style cloud application platform built on Ubuntu.

**Narrative:** I can run apps, pipelines, containers, and APIs — not just servers.

This repo is intentionally separate from my RHEL/Rocky "Linux Enterprise Lab":
- **Enterprise repo:** identity, DNS/NTP dependencies, hardening, automation (Ansible)
- **This repo:** platform delivery (Docker, CI/CD, APIs, ECS, observability, CloudWatch/SSM)

## What you'll find

- **Docs**: architecture + platform design notes
- **Labs**: reproducible, step-by-step runbooks
- **Src**: a containerized FastAPI service
- **CI/CD**: GitHub Actions pipeline (build/test → image → push → deploy)
- **Observability**: logs/metrics/alerts
- **AWS Platform**: ECS Fargate + ALB + autoscaling basics
- **No-SSH Ops**: CloudWatch + SSM Session Manager

## Quick start

Start here: `docs/00-index.md`

## Repo principles

- “Cattle, not pets”: everything should be reproducible
- Logs/metrics are first-class
- Incidents are documented as if in production
