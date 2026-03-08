"""LLM client for DeepSeek API — async enrichment layer."""

import httpx
from typing import Any


class LLMClient:
    """Async LLM client for Deauth event analysis.

    Responsibilities:
    - Explainable attribution: analyze feature vectors, explain why an event is an attack
    - Report generation: natural language security reports
    - Chat interaction: query answering and config intent recognition
    """

    def __init__(self, api_key: str, base_url: str = "https://api.deepseek.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=30.0,
            )
        return self._client

    async def analyze_event(self, event: dict) -> dict:
        """Analyze a detection event and provide explainable attribution.

        Args:
            event: Detection alert dict from RuleEngine.ingest()

        Returns:
            Dict with keys: verdict, confidence, reasoning, recommendations
        """
        # TODO: Implement DeepSeek API call with structured prompt
        # Include: frame_count, avg_rssi, MAC distribution, burst pattern
        # Return: structured JSON (verdict, confidence, reasoning)
        return {
            "verdict": "pending",
            "confidence": 0.0,
            "reasoning": "LLM analysis not yet implemented",
            "recommendations": [],
        }

    async def generate_report(self, events: list[dict]) -> str:
        """Generate a natural language security report from event history.

        Args:
            events: List of detection events with LLM attributions

        Returns:
            Markdown-formatted security report
        """
        # TODO: Implement report generation prompt
        return "Report generation not yet implemented"

    async def chat(self, message: str, context: dict[str, Any] | None = None) -> dict:
        """Process a natural language chat message.

        Supports:
        - Query: "Any attacks today?" -> analyze history and respond
        - Config: "Increase sensitivity" -> return intent + parameters
        - Explain: "Was the last attack serious?" -> contextual analysis

        Args:
            message: User's natural language input
            context: Optional context (recent events, current config, etc.)

        Returns:
            Dict with keys: reply, action (None or structured config change)
        """
        # TODO: Implement chat with function calling
        # Config changes return action dict for whitelist validation
        return {
            "reply": "Chat not yet implemented",
            "action": None,
        }

    async def close(self):
        if self._client:
            await self._client.aclose()
            self._client = None
