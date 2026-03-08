"""Alert notification service — Telegram Bot and email."""

from dataclasses import dataclass


@dataclass
class AlertConfig:
    """Alert service configuration."""
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""
    email_smtp_host: str = ""
    email_from: str = ""
    email_to: str = ""
    enabled: bool = False


class AlertService:
    """Push alert notifications via Telegram Bot or email.

    Alerts are triggered by the rule engine for high-confidence events.
    LLM attribution is appended asynchronously when available.
    """

    def __init__(self, config: AlertConfig | None = None):
        self.config = config or AlertConfig()

    async def send_alert(self, event: dict, llm_analysis: dict | None = None):
        """Send an alert notification for a detection event.

        Args:
            event: Detection alert from RuleEngine
            llm_analysis: Optional LLM attribution (may arrive later)
        """
        if not self.config.enabled:
            return

        # TODO: Format alert message
        # TODO: Send via Telegram Bot API (httpx)
        # TODO: Send via email (aiosmtplib)
        pass

    async def send_telegram(self, message: str):
        """Send a message via Telegram Bot API."""
        # TODO: Implement Telegram Bot API call
        pass

    async def send_email(self, subject: str, body: str):
        """Send an email notification."""
        # TODO: Implement email sending via aiosmtplib
        pass
