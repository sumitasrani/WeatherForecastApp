import streamlit as st
import plotly.express as px
from data import get_data

# Add title
st.title("Weather Forecast for the Next Days")

# Select Location (temporary only Mumbai)
place = st.text_input("Place:", help="Select a place")

col1, col2, col3 = st.columns([2, 0.5, 2])

with col1:
    # Forecast days
    days = st.slider("Forecast Days", min_value=1, max_value=7, help="Select the no.of days of forecast")

with col3:
    # Select Temperature or Weather
    option = st.selectbox("Select Data to View", ("Temperature", "Weather"))

# Get API data
info, value = get_data(days)

# Get time
time = info["hourly"]["time"][:value]

# Image Sort as per weather
images = {0: "images/clear.png", 1: "images/clear.png",
          2: "images/cloud.png", 3: "images/cloud.png",
          51: "images/rain.png", 53: "images/rain.png", 55: "images/rain.png",
          61: "images/rain.png", 63: "images/rain.png", 65: "images/rain.png",
          66: "images/rain.png", 67: "images/rain.png",
          80: "images/rain.png", 81: "images/rain.png", 82: "images/rain.png",
          71: "images/snow.png", 73: "images/snow.png", 75: "images/snow.png", 77: "images/snow.png"}

# Add header
st.header(f"{option} for the next {days} day in Mumbai")

# On Selection: Conditional run
if option == "Temperature":
    temperature = info["hourly"]["temperature_2m"][:value]
    figure = px.line(x=time, y=temperature, labels={"x": "Dates", "y": "Temperature (deg C)"})
    st.plotly_chart(figure)

if option == "Weather":
    weather = info["hourly"]["weathercode"][:value]
    image_path = [images[cond] for cond in weather]
    st.image(image_path, width=115)
