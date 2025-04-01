import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")

option = st.selectbox("Select data of view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

# визуал
def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10", "2022-28-10", "2022-29-10"]
    temperatures = [10, 11, 16, 20, 30]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature Celsius"},)
st.plotly_chart(figure)



