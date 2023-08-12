import streamlit as st
import plotly.express as px
from data import get_data

st.title("Weather Forecast for the Next Days")

days = st.slider("Forecast Days", min_value=1, max_value=7, help="Select the no.of days of forecast")

option = st.selectbox("Select Data to View", ("Temperature", "Weather"))

st.header(f"{option} for the next {days} day in Mumbai")

temperature, time = get_data(days, option)

figure = px.line(x=time, y=temperature, labels={"x": "Dates", "y": "Temperature (deg C)"})

st.plotly_chart(figure)
