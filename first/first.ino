#include "WiFi.h"

const char* SSID = "ESP32_A";  // Change to "ESP32_B" for second device

void setup() {
  WiFi.mode(WIFI_AP);
  WiFi.softAP(SSID);
  Serial.begin(115200);
  Serial.println("ESP32 Beacon Started: " + String(SSID));
}

void loop() {
  delay(1000);  // Just idle
}
