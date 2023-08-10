import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place:", help="Select a place")

days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the no.of days of forecast")

option = st.selectbox("Select Data to View", ("Temperature", "Sky"))

st.header(f"{option} for the next {days} in {place}")
