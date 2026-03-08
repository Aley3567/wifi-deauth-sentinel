# Firmware — ESP32 Deauth Sniffer

## Architecture

- **ESP32-A (Sniffer)**: Dedicated monitor mode, captures 802.11 management frames, never connects to WiFi
- **ESP32-B (Uplink)**: Receives data via UART from ESP32-A, connects to WiFi, publishes events over MQTT/TLS

## Build & Flash

```bash
# Install PlatformIO CLI
pip install platformio

# Build
pio run

# Flash to ESP32
pio run --target upload

# Monitor serial output
pio device monitor
```

## Hardware Connections

| ESP32-A Pin | ESP32-B Pin | Purpose |
|-------------|-------------|---------|
| TX (GPIO17) | RX (GPIO16) | UART Data |
| GND         | GND         | Common Ground |
