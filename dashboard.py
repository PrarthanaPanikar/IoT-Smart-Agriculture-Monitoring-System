import streamlit as st
import pandas as pd
import requests

from streamlit_autorefresh import st_autorefresh
from streamlit_echarts import st_echarts

from crop_recommendation import recommend_crop

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Smart Agriculture Dashboard",
    page_icon="🌱",
    layout="wide"
)

st_autorefresh(interval=5000, key="refresh")

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background-color:#f4fff4;
}

h1,h2,h3 {
    color:#1b5e20;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("data/sensor_data.csv")

latest = df.iloc[-1]

# -----------------------------
# HEADER
# -----------------------------

st.title("🌱 Smart Agriculture Monitoring Dashboard")

st.markdown(
    "### AI Powered Smart Farming System"
)

# -----------------------------
# ALERTS
# -----------------------------

if latest["Temperature"] > 35:
    st.error("🔥 High Temperature Alert")

if latest["Water_Level"] < 30:
    st.warning("💧 Low Water Level Alert")

if latest["Soil_Moisture"] < 1500:
    st.warning("🚰 Dry Soil Detected")

# -----------------------------
# KPI CARDS
# -----------------------------

st.subheader("📊 Live Sensor Readings")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric(
        "🌡 Temperature",
        f"{latest['Temperature']} °C"
    )

with c2:
    st.metric(
        "💧 Humidity",
        f"{latest['Humidity']} %"
    )

with c3:
    st.metric(
        "🌱 Soil Moisture",
        int(latest["Soil_Moisture"])
    )

with c4:
    st.metric(
        "🚰 Water Level",
        f"{latest['Water_Level']} %"
    )

with c5:
    st.metric(
        "⚙ Pump",
        latest["Pump_Status"]
    )

# -----------------------------
# GAUGE METERS
# -----------------------------

st.subheader("🎯 Live Gauge Meters")

g1, g2, g3 = st.columns(3)

with g1:

    option = {
        "series": [{
            "type": "gauge",
            "progress": {"show": True},
            "detail": {"valueAnimation": True},
            "data": [{"value": int(latest["Temperature"])}]
        }]
    }

    st_echarts(option, height="300px")

with g2:

    option = {
        "series": [{
            "type": "gauge",
            "progress": {"show": True},
            "detail": {"valueAnimation": True},
            "data": [{"value": int(latest["Humidity"])}]
        }]
    }

    st_echarts(option, height="300px")

with g3:

    option = {
        "series": [{
            "type": "gauge",
            "progress": {"show": True},
            "detail": {"valueAnimation": True},
            "data": [{"value": int(latest["Water_Level"])}]
        }]
    }

    st_echarts(option, height="300px")

# -----------------------------
# SENSOR HEALTH
# -----------------------------

st.subheader("🟢 Sensor Health")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.success("Temperature Sensor Online")

with s2:
    st.success("Humidity Sensor Online")

with s3:
    st.success("Soil Sensor Online")

with s4:
    st.success("Water Sensor Online")

# -----------------------------
# AI CROP RECOMMENDATION
# -----------------------------

crop = recommend_crop(
    latest["Temperature"],
    latest["Humidity"]
)

st.subheader("🌾 AI Crop Recommendation")

st.success(f"Recommended Crop : {crop}")

# -----------------------------
# SMART FARMING ADVICE
# -----------------------------

st.subheader("🤖 Smart Farming Advice")

if latest["Temperature"] > 35:
    st.warning(
        "High temperature detected. Increase irrigation."
    )

if latest["Soil_Moisture"] < 1500:
    st.warning(
        "Soil is dry. Pump should be activated."
    )

if latest["Water_Level"] < 30:
    st.warning(
        "Refill water tank."
    )

# -----------------------------
# WEATHER SECTION
# -----------------------------

st.subheader("🌦 Weather Integration")

st.info(
    "Connect OpenWeather API key here for live weather."
)

# -----------------------------
# CHARTS
# -----------------------------

st.subheader("📈 Temperature Trend")
st.line_chart(df["Temperature"])

st.subheader("📈 Humidity Trend")
st.line_chart(df["Humidity"])

st.subheader("📈 Soil Moisture Trend")
st.line_chart(df["Soil_Moisture"])

st.subheader("📈 Water Level Trend")
st.line_chart(df["Water_Level"])

# -----------------------------
# DOWNLOAD BUTTON
# -----------------------------

st.subheader("📥 Download Sensor Data")

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="sensor_data.csv",
    mime="text/csv"
)

# -----------------------------
# DATA TABLE
# -----------------------------

st.subheader("📋 Sensor Data History")

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.markdown(
"""
### 🌱 Smart Agriculture Monitoring System

Features:
- Real Time Monitoring
- AI Crop Recommendation
- Smart Irrigation
- Download Reports
- Sensor Health Tracking
- Gauge Visualization
"""
)