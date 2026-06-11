import logging

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette.status import HTTP_303_SEE_OTHER

from app.db import get_db, init_db
from app.models import Todo

# -------------------
# LOGGING
# -------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

logger = logging.getLogger(__name__)

# -------------------
# APP
# -------------------
app = FastAPI(title="Todo App", version="1.0.0")

Instrumentator().instrument(app).expose(app)

templates = Jinja2Templates(directory="app/templates")


# -------------------
# INIT DB
# -------------------
@app.on_event("startup")
def startup():
    logger.info("Initializing DB...")
    init_db()


# -------------------
# HEALTH
# -------------------
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ready"}


# -------------------
# HOME PAGE (HTML)
# -------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    try:
        todos = db.query(Todo).order_by(Todo.id.desc()).all()
    except Exception as e:
        logger.error(f"DB error: {e}")
        todos = []

    return templates.TemplateResponse(request, "index.html", {"todos": todos or []})


# -------------------
# CREATE TODO (FORM)
# -------------------
@app.post("/todos")
def create(title: str = Form(...), db: Session = Depends(get_db)):
    todo = Todo(title=title, done=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)

    logger.info(f"Created todo {todo.id}")

    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


# -------------------
# MARK DONE
# -------------------
@app.post("/todos/{todo_id}/done")
def done(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        return {"error": "not found"}

    todo.done = True
    db.commit()

    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


# -------------------
# DELETE TODO
# -------------------
@app.post("/todos/{todo_id}/delete")
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        return {"error": "not found"}

    db.delete(todo)
    db.commit()

    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
