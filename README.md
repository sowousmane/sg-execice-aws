# FastAPI Todo App

Simple FastAPI application using PostgreSQL, Docker, and Pytest.

This project also includes observability tools (Grafana, Loki, Promtail).

---

## Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pytest
- Docker / Docker Compose
- Grafana
- Loki
- Promtail


---

## Environment variables

The project requires a `.env` file based on `.env.template`.

Create it with:

```bash
cp .env.template .env
````

Main variables:

```env
DATABASE_URL=postgresql://user:password@db:5432/app
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=app
```

---

## Run the project

Start all services:

```bash
docker compose up --build
```

Application:

[http://localhost:8000](http://localhost:8000)

---

## Run tests

Tests should be executed inside a virtual environment:

```bash
PYTHONPATH=. DATABASE_URL=sqlite:///./test.db pytest -q
```

---

## Docker

Build image:

```bash
docker build -t fastapi-app .
```

Run container:

```bash
docker run -p 8000:8000 fastapi-app
```

---

## Observability

This project includes:

* Grafana (dashboards)
* Loki (logs aggregation)
* Promtail (log shipping)

Start them via Docker Compose:

```bash
docker compose up -d
```

---

## API

Once running:

* [http://localhost:8000](http://localhost:8000) → API root
* [http://localhost:8000/docs](http://localhost:8000/docs) → Swagger UI

---

## Next steps

* GitHub Actions CI/CD pipeline
* Traefik reverse proxy with HTTPS (Cloudflare)
* Push Docker images to Docker Hub
* Security scanning with Trivy
* Automated deployment on AWS EC2 (no manual SSH steps)

---

## Notes

* Ensure PostgreSQL is running before starting the app
* Use `.env.template` as reference for configuration
* All services are containerized via Docker Compose

```