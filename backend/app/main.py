from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router

app = FastAPI(
    title="WiFi Deauth Sentinel",
    description="WiFi deauthentication attack detection system with LLM-powered analysis",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.on_event("startup")
async def startup_event():
    # TODO: Initialize SQLite database tables
    # TODO: Start MQTT subscriber in background task
    # TODO: Initialize rule engine with default config
    pass


@app.on_event("shutdown")
async def shutdown_event():
    # TODO: Gracefully disconnect MQTT
    # TODO: Close database connections
    pass
