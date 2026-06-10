import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("data/sensor_data.csv")

# Temperature Graph
plt.figure(figsize=(8,5))
plt.plot(df["Temperature"])
plt.title("Temperature Trend")
plt.xlabel("Readings")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.savefig("outputs/temperature_graph.png")
plt.close()

# Humidity Graph
plt.figure(figsize=(8,5))
plt.plot(df["Humidity"])
plt.title("Humidity Trend")
plt.xlabel("Readings")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.savefig("outputs/humidity_graph.png")
plt.close()

# Soil Moisture Graph
plt.figure(figsize=(8,5))
plt.plot(df["Soil_Moisture"])
plt.title("Soil Moisture Trend")
plt.xlabel("Readings")
plt.ylabel("Soil Moisture")
plt.grid(True)
plt.savefig("outputs/soil_moisture_graph.png")
plt.close()

print("✅ All graphs generated successfully!")