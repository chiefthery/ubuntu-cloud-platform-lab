
# Ubuntu Cloud Platform Lab

This repository documents a hands-on cloud platform engineering project focused on building, deploying, and operating a containerized API service on Ubuntu Linux.

The project follows a production-style workflow: application → container → automation → cloud deployment → scaling → monitoring.

---

## Objectives

- Build a Linux-hosted API service
- Containerize applications using Docker
- Implement CI/CD pipelines
- Deploy to AWS container infrastructure
- Configure scaling and logging
- Practice platform operations

---

## Stack

- Ubuntu Linux (AWS EC2)
- Python + FastAPI
- Docker
- GitHub Actions
- AWS (ECR, ECS, ALB, CloudWatch)
- Terraform

---

## Roadmap

### Week 1 — API + Containerization

- FastAPI service

- `/health` and `/info` endpoints

- Local execution on Ubuntu

- Docker build and run

### Week 2 — CI/CD + Deployment

- GitHub Actions pipeline
- Push images to ECR
- Deploy to ECS

### Week 3 — Scaling + Observability

- Application Load Balancer
- Autoscaling policies
- Centralized logging
- Metrics monitoring

---

## Repository Structure

- **apps/:** Application source code
- **.github/:** CI/CD workflows
- **terraform/:** Cloud infrastructure
- **docs/:** Technical writeups and incidents


