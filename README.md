## 🌱 IoT Smart Agriculture Monitoring System

An AI-powered Smart Agriculture Monitoring System that simulates IoT sensors, automates irrigation decisions, logs environmental data, generates analytics, and provides a professional real-time dashboard for precision farming.

---

# 📑 Table of Contents

* [Project Overview](#-project-overview)
* [Features](#-features)
* [Technology Stack](#-technology-stack)
* [Project Architecture](#-project-architecture)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [Running the Project](#-running-the-project)
* [Dashboard Features](#-dashboard-features)
* [AI Crop Recommendation](#-ai-crop-recommendation)
* [Graphs & Analytics](#-graphs--analytics)
* [Future Enhancements](#-future-enhancements)
* [Screenshots](#-screenshots)
* [Learning Outcomes](#-learning-outcomes)
* [Author](#-author)

---

# 🌾 Project Overview

The Smart Agriculture Monitoring System is designed to simulate an IoT-enabled farming environment where multiple sensors continuously monitor agricultural conditions.

The system:

* Monitors environmental parameters
* Generates alerts automatically
* Controls irrigation logic
* Stores sensor readings
* Visualizes historical trends
* Provides AI-based crop recommendations
* Displays data through a professional dashboard

---

# 🚀 Features

## Sensor Monitoring

* 🌡 Temperature Monitoring
* 💧 Humidity Monitoring
* 🌱 Soil Moisture Monitoring
* ☀ Light Intensity Monitoring
* 🚰 Water Level Monitoring

## Automation

* Automatic Pump Control
* Dry Soil Detection
* Water Level Monitoring
* Alert Generation

## Data Analytics

* CSV Data Logging
* Temperature Trend Analysis
* Humidity Trend Analysis
* Soil Moisture Trend Analysis
* Water Level Trend Analysis

## Dashboard

* Real-Time Monitoring
* Auto Refresh
* KPI Cards
* Gauge Meters
* Sensor Health Indicators
* Download CSV Reports

## AI Features

* Crop Recommendation
* Smart Farming Suggestions

---

# 🛠 Technology Stack

| Technology        | Purpose               |
| ----------------- | --------------------- |
| Python            | Core Programming      |
| Pandas            | Data Processing       |
| Matplotlib        | Data Visualization    |
| Streamlit         | Dashboard Development |
| Streamlit ECharts | Gauge Meters          |
| CSV               | Data Storage          |
| Git               | Version Control       |
| GitHub            | Project Hosting       |

---

# 🏗 Project Architecture

Sensor Simulation
↓
Data Collection
↓
CSV Data Logging
↓
Data Analysis
↓
Dashboard Visualization
↓
AI Recommendations
↓
Farmer Decision Support

---

# 📂 Project Structure

```text
IoT-Smart-Agriculture-Monitoring-System
│
├── main.py
├── dashboard.py
├── graph.py
├── crop_recommendation.py
├── README.md
├── requirements.txt
│
├── data
│   └── sensor_data.csv
│
├── outputs
│   ├── temperature_graph.png
│   ├── humidity_graph.png
│   └── soil_moisture_graph.png
│
├── images
│   ├── project_structure.png
│   ├── sensor_monitoring.png
│   ├── dashboard.png
│   └── graphs.png
│
├── arduino_code
├── docs
└── circuit_diagram
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/PrarthanaPanikar/IoT-Smart-Agriculture-Monitoring-System.git
```

## Move Into Project Folder

```bash
cd IoT-Smart-Agriculture-Monitoring-System
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Run Sensor Simulation

```bash
python main.py
```

## Generate Graphs

```bash
python graph.py
```

## Launch Dashboard

```bash
streamlit run dashboard.py
```

---

# 📊 Dashboard Features

The Streamlit dashboard provides:

* Live Sensor Monitoring
* KPI Cards
* Temperature Analysis
* Humidity Analysis
* Soil Moisture Analysis
* Water Level Analysis
* Sensor Health Tracking
* Download CSV Option
* Auto Refresh Every 5 Seconds

---

# 🌾 AI Crop Recommendation

The system recommends crops using:

* Temperature
* Humidity
* Environmental Conditions

Supported Recommendations:

* Rice
* Wheat
* Maize
* Vegetables

---

# 📈 Graphs & Analytics

Generated Analytics:

* Temperature Trend
* Humidity Trend
* Soil Moisture Trend
* Water Level Trend

Output files are automatically saved in the `outputs` folder.

---

# 🔮 Future Enhancements

* Weather API Integration
* Farm Location Mapping
* Email Alert System
* Mobile Application
* Arduino Integration
* ESP32 Connectivity
* MQTT Communication
* Machine Learning Prediction
* Crop Disease Detection
* Smart Irrigation Scheduling

---

# 📸 Screenshots

## Dashboard
<img width="1366" height="668" alt="Screenshot 2026-06-10 132420" src="https://github.com/user-attachments/assets/566e38c5-eec6-4ed2-839c-4aa04aed3149" />
<img width="1360" height="665" alt="Screenshot 2026-06-10 132449" src="https://github.com/user-attachments/assets/37fc4d47-1773-4291-91d3-bba19a2006d3" />



## Sensor Monitoring

<img width="1366" height="661" alt="Screenshot 2026-06-10 123203" src="https://github.com/user-attachments/assets/d2796750-7b9e-4e52-a0d3-3ee2d21292be" />

<img width="1366" height="649" alt="Screenshot 2026-06-10 123310" src="https://github.com/user-attachments/assets/69343691-df39-4095-9162-d7cf0ed68d19" />

<img width="1366" height="641" alt="Screenshot 2026-06-10 123325" src="https://github.com/user-attachments/assets/f8898a43-ec42-4355-bdd5-e08db97feb52" />

<img width="1281" height="648" alt="Screenshot 2026-06-10 123348" src="https://github.com/user-attachments/assets/edb21638-7140-48d2-a172-d95ec4d0e700" />


## Analytics Graphs

<img width="1366" height="664" alt="Screenshot 2026-06-10 132532" src="https://github.com/user-attachments/assets/9aaee2a7-a47d-489b-acb1-fca0dd371745" />

<img width="1364" height="637" alt="Screenshot 2026-06-10 132604" src="https://github.com/user-attachments/assets/ac8252fe-5a58-4a1c-80fe-b52e46076764" />

<img width="1366" height="627" alt="Screenshot 2026-06-10 132620" src="https://github.com/user-attachments/assets/bf83f3d7-fb96-4dc0-8938-0a6c77cbee7c" />

<img width="1366" height="635" alt="Screenshot 2026-06-10 132655" src="https://github.com/user-attachments/assets/7c4b4461-59b2-4042-a465-a1d4951e4488" />


# 🎯 Learning Outcomes

This project demonstrates:

* Internet of Things (IoT)
* Sensor Data Simulation
* Data Logging
* Data Analytics
* Dashboard Development
* Automation Logic
* Python Programming
* Git & GitHub Workflow
* Real-Time Monitoring Systems

---

# 👩‍💻 Author

**Prarthana Panikar**

B.Tech Computer Science

GitHub:
https://github.com/PrarthanaPanikar

---

⭐ If you found this project useful, please give it a star on GitHub.
