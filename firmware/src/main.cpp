#include <Arduino.h>

// TODO: Step 1 - Implement WiFi promiscuous mode for Deauth frame capture
// - Enable monitor mode via esp_wifi_set_promiscuous()
// - Register callback for management frame filtering
// - Extract: source MAC, destination MAC, RSSI, channel
// - Sliding window pre-filter to reduce uplink traffic

// TODO: Step 2 - UART communication to ESP32-B for MQTT uplink
// - Serialize detection events as JSON
// - Send via Serial/UART to the uplink board

void setup() {
    Serial.begin(115200);
    Serial.println("[Sentinel] ESP32 Deauth Sniffer - Booting...");

    // TODO: Initialize WiFi in promiscuous mode
    // TODO: Initialize OLED display (optional)
    // TODO: Initialize LED + buzzer for physical alert
}

void loop() {
    // TODO: Main detection loop
    // Frame capture is handled via promiscuous callback
    // This loop handles:
    // - Sliding window evaluation
    // - UART data transmission
    // - OLED status update
    delay(100);
}
