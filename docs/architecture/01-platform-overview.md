# Platform Overview

## Goal

Demonstrate production-style platform engineering on Ubuntu:
- containerized services
- CI/CD pipelines
- observability
- AWS application platform (ECS Fargate + ALB)
- operational access via SSM Session Manager (no SSH)

## Architecture (target end-state)

Developer workflow:
1) `git push`
2) GitHub Actions runs tests + builds container
3) Image pushed to ECR
4) ECS service deploys new version behind ALB
5) Logs/metrics shipped to CloudWatch; alerts configured
6) Ops access via SSM Session Manager

## Why Ubuntu

Ubuntu is common for cloud-native application platforms and integrates smoothly with:
- Docker/containers
- GitHub Actions runners
- cloud SDKs and tooling

## Separation from Enterprise Lab

This repo intentionally avoids:
- FreeIPA / enterprise identity
- RHEL-centric hardening depth
- “pet server” operational patterns

Instead it focuses on:
- reproducible platform delivery
- “cattle not pets”
