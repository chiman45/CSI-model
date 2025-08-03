import serial
import csv
import time
import math

# Open serial port (change COM port as needed)
ser = serial.Serial('COM5', 115200)  # Replace 'COM5' with your port (e.g., /dev/ttyUSB0)
time.sleep(2)

with open("esp32_rssi_dataset.csv", mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["RSSI_A", "RSSI_B", "xA", "yA", "angleA", "xB", "yB", "angleB", "Person"])

    while True:
        try:
            line = ser.readline().decode().strip()
            if "," not in line:
                continue
            rssiA_str, rssiB_str = line.split(",")
            rssiA = int(rssiA_str)
            rssiB = int(rssiB_str)

            # Simulate position: assume ESP_A at (0,0), ESP_B at (2,0), Person in middle
            xA, yA = 1.0, 1.0
            xB, yB = -1.0, 1.0

            angleA = round(math.degrees(math.atan2(yA, xA)), 2)
            angleB = round(math.degrees(math.atan2(yB, xB)), 2)

            writer.writerow([rssiA, rssiB, xA, yA, angleA, xB, yB, angleB, ""])
            print(f"Saved: RSSI_A={rssiA}, RSSI_B={rssiB}")
        except KeyboardInterrupt:
            print("Logging stopped.")
            break
