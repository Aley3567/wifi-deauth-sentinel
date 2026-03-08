"""MQTT subscriber for receiving ESP32 detection events."""

import json
import paho.mqtt.client as mqtt
from typing import Callable


class MQTTSubscriber:
    """Subscribe to MQTT topics for ESP32 Deauth detection events.

    Topics:
    - sentinel/events    : Raw detection events from ESP32-B
    - sentinel/status    : Device heartbeat and status updates
    - sentinel/control   : Control messages to ESP32 (config updates)
    """

    TOPIC_EVENTS = "sentinel/events"
    TOPIC_STATUS = "sentinel/status"
    TOPIC_CONTROL = "sentinel/control"

    def __init__(
        self,
        host: str = "localhost",
        port: int = 1883,
        on_event: Callable[[dict], None] | None = None,
    ):
        self.host = host
        self.port = port
        self._on_event = on_event
        self._client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

        self._client.on_connect = self._handle_connect
        self._client.on_message = self._handle_message

    def _handle_connect(self, client, userdata, flags, reason_code, properties):
        """Subscribe to topics on successful connection."""
        client.subscribe(self.TOPIC_EVENTS)
        client.subscribe(self.TOPIC_STATUS)

    def _handle_message(self, client, userdata, msg):
        """Route incoming messages to appropriate handlers."""
        try:
            payload = json.loads(msg.payload.decode())
        except (json.JSONDecodeError, UnicodeDecodeError):
            return

        if msg.topic == self.TOPIC_EVENTS and self._on_event:
            self._on_event(payload)

        # TODO: Handle status topic for device health monitoring

    def connect(self):
        """Connect to MQTT broker and start listening."""
        # TODO: Add TLS configuration for production
        self._client.connect(self.host, self.port, keepalive=60)

    def start(self):
        """Start the MQTT event loop (blocking)."""
        self.connect()
        self._client.loop_forever()

    def start_background(self):
        """Start the MQTT event loop in a background thread."""
        self.connect()
        self._client.loop_start()

    def publish_control(self, payload: dict):
        """Publish a control message to ESP32."""
        self._client.publish(self.TOPIC_CONTROL, json.dumps(payload))

    def stop(self):
        """Stop the MQTT client."""
        self._client.loop_stop()
        self._client.disconnect()
