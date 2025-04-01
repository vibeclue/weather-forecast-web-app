import streamlit as st
import plotly.express as px

from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")

option = st.selectbox("Select data of view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

# визуал


d, t = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature Celsius"},)
st.plotly_chart(figure)



