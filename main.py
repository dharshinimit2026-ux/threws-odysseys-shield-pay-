from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import APP_NAME
from .database import Base, engine
from . import models  # noqa: F401 - registers SQLAlchemy models
from .routes import payments, history, risk

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    description="Educational bank-side remote-access fraud protection prototype. Not an SBI integration.",
    version="1.0.0",
)

# Local frontend development only. Restrict origins before any real deployment.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/", tags=["System"])
def home():
    return {
        "project": APP_NAME,
        "status": "running",
        "notice": "Prototype only. No live SBI connection or real payment blocking."
    }

@app.get("/health", tags=["System"])
def health():
    return {"status": "healthy"}

app.include_router(payments.router)
app.include_router(history.router)
app.include_router(risk.router)
