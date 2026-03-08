from fastapi import APIRouter

router = APIRouter()


@router.get("/events")
async def list_events():
    """List all detected deauth events with pagination."""
    # TODO: Query SQLite for events, support pagination and filters
    return {"events": [], "total": 0}


@router.get("/events/{event_id}")
async def get_event(event_id: int):
    """Get a single event with LLM attribution details."""
    # TODO: Fetch event by ID, include LLM analysis if available
    return {"error": "not implemented"}


@router.post("/chat")
async def chat(message: dict):
    """Natural language chat interface powered by LLM.

    Supports:
    - Query: "Any attacks today?" -> LLM analyzes history and responds
    - Config: "Increase sensitivity" -> whitelist mapping -> user confirmation -> execute
    - Explain: "Was the last attack serious?" -> LLM contextual analysis
    """
    # TODO: Parse user message, route to LLM with function calling
    # TODO: Config changes must go through whitelist + confirmation
    return {"reply": "Chat endpoint not yet implemented"}


@router.get("/config")
async def get_config():
    """Get current detection configuration."""
    # TODO: Return rule engine parameters (window_size, threshold, etc.)
    return {"window_size": 5, "threshold": 10}


@router.put("/config")
async def update_config(config: dict):
    """Update detection configuration (whitelist-gated)."""
    # TODO: Validate against whitelist of allowed config changes
    return {"status": "not implemented"}
