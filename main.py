import random
import time
import csv
from datetime import datetime

# Create CSV file if not exists
with open("data/sensor_data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Timestamp",
        "Temperature",
        "Humidity",
        "Soil_Moisture",
        "Light_Intensity",
        "Water_Level",
        "Pump_Status"
    ])

while True:

    temperature = random.randint(25, 40)
    humidity = random.randint(40, 90)
    soil_moisture = random.randint(1000, 3000)
    light_intensity = random.randint(100, 1000)
    water_level = random.randint(10, 100)

    pump_status = "ON" if soil_moisture < 1500 else "OFF"

    print("\n====================================")
    print("SMART AGRICULTURE MONITORING SYSTEM")
    print("====================================")

    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Soil Moisture:", soil_moisture)
    print("Light Intensity:", light_intensity)
    print("Water Level:", water_level, "%")
    print("Pump Status:", pump_status)

    # Save to CSV
    with open("data/sensor_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now(),
            temperature,
            humidity,
            soil_moisture,
            light_intensity,
            water_level,
            pump_status
        ])

    print("✅ Data Logged Successfully")

    time.sleep(5)