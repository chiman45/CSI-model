#include "WiFi.h"

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
}

void loop() {
  int n = WiFi.scanNetworks();
  int rssiA = 0, rssiB = 0;
  for (int i = 0; i < n; ++i) {
    String ssid = WiFi.SSID(i);
    int rssi = WiFi.RSSI(i);
    if (ssid == "ESP32_A") rssiA = rssi;
    if (ssid == "ESP32_B") rssiB = rssi;
  }

  // Format: RSSI_A, RSSI_B
  Serial.print(rssiA);
  Serial.print(",");
  Serial.println(rssiB);
  
  delay(2000); // Rescan every 2s
}
