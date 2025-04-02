import streamlit as st
import plotly.express as px

from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input("Place: ")


days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")

option = st.selectbox("Select data of view", ("Temperature", "Sky"))

if not place:
    place = 'Brest'

st.subheader(f"{option} for the next {days} days in {place}")

# данные
filtered_data = get_data(place, days)

# визуал
if option == 'Temperature':
    temperatures = [dict['main']['temp'] for dict in filtered_data]
    dates = [dict['dt_txt'] for dict in filtered_data]
    figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature Celsius"}, )
    st.plotly_chart(figure)

elif option == 'Sky':
    sky_data = ["images/" + dict['weather'][0]['main'].lower() + ".png" for dict in filtered_data]
    print(sky_data)
    st.image(sky_data, width=115)





