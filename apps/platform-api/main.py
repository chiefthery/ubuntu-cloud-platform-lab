from fastapi import FastAPI
from datetime import datetime, timezone
import os

app = FastAPI(
    title="platform-api",
    version=os.getenv("APP_VERSION", "0.1.0"),
)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/info")
def info():
    return {
        "service": app.title,
        "version": app.version,
        "environment": os.getenv("ENVIRONMENT", "dev"),
    }

