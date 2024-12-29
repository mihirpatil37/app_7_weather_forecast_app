import streamlit as st
import plotly.express as px
from backend import get_weather_data

# UI Components: title, text input, slider, select-box, and sub-header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")

days = st.slider("Select the number of forecast days:", min_value=1, max_value=5)

option = st.selectbox("Select data to view",("Temperature", "Sky"))

if place:
    st.subheader(f"{option} forecast for the next {days} days in {place}")
    try:
        if place:
            # Get the temperature/sky data
            filtered_data = get_weather_data(place, days)
            if option == "Temperature":
                temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
                dates = [dict["dt_txt"] for dict in filtered_data]
                # Create a temperature plot
                figure= px.line(x=dates,y= temperatures, labels={"x":"Date", "y":"Temperature(C)"})
                st.plotly_chart(figure)

            if option == "Sky":

                images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                          "Rain": "images/rain.png", "Snow": "images/snow.png"}


                sky_conditions= [dict["weather"][0]["main"] for dict in filtered_data]
                image_path = [images[conditions] for conditions in sky_conditions]
                st.image(image_path, width=115)


    except KeyError:'"The entered place is not found!" Please enter a valid place.'


