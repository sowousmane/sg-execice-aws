# 🚀 DevSecOps Observability Stack

This project demonstrates a complete DevSecOps workflow from code commit to deployment on AWS EC2, including CI/CD automation, security scanning, and full observability (metrics, logs, dashboards).

---
## 🧭 Architecture Overview
### 🔄 CI/CD Pipeline

Developer → GitHub → CI (lint / tests / security) → Docker build → Registry → CD → EC2

---
### 📦 Runtime Architecture

Application → Prometheus (metrics)
→ Loki (logs)
→ Grafana (dashboards)

---
## 🖥️ Run the project locally
### 📌 Prerequisites
Make sure you have installed:
- Docker
- Docker Compose 

### 🚀 Start the stack

From the project root:

docker compose up -d --build



###  📊 Access services

Service	URL
Application	http://localhost:8000  
Grafana	http://localhost:3000



###  🧪 Tests

PYTHONPATH=. DATABASE_URL=sqlite:///./test.db pytest -q



###  🧱 Tech Stack

CI/CD

* GitHub Actions / GitLab CI
* Docker
* Trivy (security scanning)

Infrastructure

* AWS EC2
* Docker Compose

Observability

* Prometheus (metrics)
* Loki (logs)
* Grafana (visualization)



🔐 Security Highlights

* Container vulnerability scanning (Trivy)
* Isolated services via Docker Compose
* Future: SAST / DAST integration



🚀 Deployment Flow

1. Code push
2. CI pipeline (lint / test / scan)
3. Docker image build
4. Push to registry (ECR / Docker Hub)
5. Deploy to EC2 (SSH / SSM)

**Tech stack**

- Application: Python / FastAPI
- Reverse proxy: Traefik (ACME / Let's Encrypt)
- Database: PostgreSQL
- Observability: Loki, Grafana
- CI/CD: GitHub Actions / GitLab CI (examples)

**Next improvements**

- IaC: Terraform for EC2, Security Groups, VPC
- Production: ACME DNS challenge with Cloudflare token, SSM/Ansible deployment, monitoring alerts

 
