"""Sliding window rule engine for Deauth frame detection."""

from dataclasses import dataclass, field
from collections import deque
import time


@dataclass
class DetectionConfig:
    """Detection parameters."""
    window_size: float = 5.0        # Sliding window in seconds
    threshold: int = 10             # Deauth frames to trigger alert
    cooldown: float = 30.0          # Seconds between repeated alerts for same source


@dataclass
class FrameEvent:
    """A single captured Deauth frame."""
    timestamp: float
    channel: int
    rssi: int
    src_mac: str
    dst_mac: str


class RuleEngine:
    """Sliding window Deauth detection engine.

    Runs purely local — no network or LLM dependency.
    Designed to work both on ESP32 (simplified) and backend (full).
    """

    def __init__(self, config: DetectionConfig | None = None):
        self.config = config or DetectionConfig()
        self._window: deque[FrameEvent] = deque()
        self._last_alert: dict[str, float] = {}  # src_mac -> last alert timestamp

    def ingest(self, frame: FrameEvent) -> dict | None:
        """Ingest a frame and return an alert dict if threshold exceeded.

        Returns None if no alert, or a dict with detection details
        including a 'confidence' field:
          - 'high': clearly above threshold
          - 'gray': borderline, should be sent to LLM for second opinion
        """
        now = frame.timestamp
        self._window.append(frame)

        # Evict frames outside the sliding window
        while self._window and (now - self._window[0].timestamp) > self.config.window_size:
            self._window.popleft()

        count = len(self._window)
        if count < self.config.threshold:
            return None

        # Cooldown check
        src = frame.src_mac
        if src in self._last_alert:
            if (now - self._last_alert[src]) < self.config.cooldown:
                return None

        self._last_alert[src] = now

        # Determine confidence zone
        ratio = count / self.config.threshold
        confidence = "high" if ratio >= 2.0 else "gray"

        # Collect unique MACs for feature vector
        src_macs = set(f.src_mac for f in self._window)
        dst_macs = set(f.dst_mac for f in self._window)

        return {
            "timestamp": now,
            "frame_count": count,
            "window_size": self.config.window_size,
            "confidence": confidence,
            "src_macs": list(src_macs),
            "dst_macs": list(dst_macs),
            "avg_rssi": sum(f.rssi for f in self._window) / count,
            "channels": list(set(f.channel for f in self._window)),
        }

    def update_config(self, **kwargs):
        """Update detection parameters at runtime."""
        for key, value in kwargs.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)
