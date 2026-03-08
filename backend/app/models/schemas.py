"""Pydantic models for API request/response schemas."""

from pydantic import BaseModel
from datetime import datetime


class DeauthEvent(BaseModel):
    """A detected deauthentication event."""
    id: int | None = None
    timestamp: datetime
    channel: int
    rssi: int
    src_mac: str
    dst_mac: str
    frame_count: int
    confidence: str = "high"         # "high" or "gray"
    llm_verdict: str | None = None   # LLM attribution result
    llm_reasoning: str | None = None # LLM explanation


class AlertResponse(BaseModel):
    """Alert notification payload."""
    event_id: int
    severity: str                    # "critical", "warning", "info"
    title: str
    description: str
    timestamp: datetime


class ChatMessage(BaseModel):
    """Chat request from frontend."""
    message: str
    session_id: str | None = None


class ChatResponse(BaseModel):
    """Chat response to frontend."""
    reply: str
    action: dict | None = None       # Structured config change if applicable
    requires_confirmation: bool = False


class DetectionConfigSchema(BaseModel):
    """Detection engine configuration."""
    window_size: float = 5.0
    threshold: int = 10
    cooldown: float = 30.0
