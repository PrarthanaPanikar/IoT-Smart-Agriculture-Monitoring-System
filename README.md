## 🌱 IoT Smart Agriculture Monitoring System



\

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

Add dashboard screenshot here.

```text
images/dashboard.png
```

## Sensor Monitoring

Add terminal monitoring screenshot here.

```text
images/sensor_monitoring.png
```

## Analytics Graphs

Add graph screenshots here.

```text
images/graphs.png
```

---

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

B.Tech Computer Science\

GitHub:
https://github.com/PrarthanaPanikar

---

⭐ If you found this project useful, please give it a star on GitHub.
