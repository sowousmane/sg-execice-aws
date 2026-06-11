Voici une version “lazy dev mais pro” : simple, lisible, mais suffisamment clean pour GitHub + entretien DevSecOps.

⸻

:::writing{variant=“document” id=“91873”}

🚀 FastAPI Todo App (DevSecOps Stack)

Simple Todo application built with FastAPI, PostgreSQL and Docker.
Includes observability (Grafana, Loki, Promtail), CI/CD, and Traefik reverse proxy.

⸻

⚙️ Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker / Docker Compose
* Traefik (reverse proxy)
* Grafana + Loki + Promtail
* Pytest
* Prometheus metrics

⸻

🏃 Run locally

docker compose up -d --build

⸻

🌍 Access

Local (dev mode)

Add to /etc/hosts:

127.0.0.1 my-todo-sg.localhost
127.0.0.1 monito-sg.localhost

Then:

* API → http://my-todo-sg.localhost
* Monitoring → http://monito-sg.localhost

⸻

Production (AWS - next step)

* API → https://my-todo-sg.soowcode.com
* Grafana → https://monito-sg.soowcode.com

⸻

🔎 API endpoints

Health

* GET /health → service status
* GET /ready → DB readiness check

App

* GET / → HTML todo list
* POST /todos → create todo
* POST /todos/{id}/done → mark as done
* POST /todos/{id}/delete → delete todo

Metrics

* GET /metrics → Prometheus metrics

⸻

📊 Observability

* Grafana → dashboards
* Loki → logs aggregation
* Promtail → log shipping from Docker

⸻

🔐 Security

* No direct DB exposure
* Services isolated via Docker networks
* Traefik reverse proxy handles routing
* .env and acme.json excluded from Git
* Image scanning via Trivy (CI pipeline)

⸻

🚀 CI/CD

Pipeline includes:

* Tests (Pytest)
* Build Docker image
* Security scan (Trivy)
* Push to DockerHub
* Deployment step (AWS EC2 – next step)

⸻

🧪 Tests

PYTHONPATH=. DATABASE_URL=sqlite:///./test.db pytest -q

⸻

🐳 Docker

Build:

docker build -t fastapi-app .

Run:

docker run -p 8000:8000 fastapi-app

⸻

🧭 Roadmap

* AWS EC2 deployment (next step)
* Terraform infrastructure
* HTTPS hardening (HSTS, headers, WAF)

⸻
