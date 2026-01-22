import streamlit as st
import pandas as pd
import httpx

URL = "http://127.0.0.1:8000"
data = httpx.get(f"{URL}/taxi/data")
df = pd.DataFrame(data.json())

def main():
    page = st.sidebar.radio(
        "Navigation",
        ["Home", "Predict price", "View data"]
    )

    if page == "Home":
        st.title("Taxi prediction app")
        st.write( """
                 This application allows you to explore taxi trips and predict the price of a ride
                based on several factors such as distance, time of day, weather, and traffic.
                The model is trained on a real-world dataset and uses machine learning
                to provide an estimate of the expected fare.
                
                Use the sidebar to view data or make a price prediction.
                """

        )

    if page == "View data":
        with st.expander("Show taxi dataset"):
            st.dataframe(
                df,
                height=300,
                use_container_width=True
            )
    if page == "Predict price":
        st.markdown("## Predict Taxi Price")

        with st.form("prediction_form"):
            Trip_Distance_km = st.number_input("Trip Distance (km)", min_value=0.1, max_value=155.0, value=5.0)
            Trip_Duration_Minutes = st.number_input(
            "Estimated trip duration (minutes)\n(If unsure, choose a typical value for the distance)",
            min_value=1.0,
            max_value=125.0,
            value=10.0
            )
            

            Time_of_Day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
            Day_of_Week = st.selectbox("Day of Week", ["Weekday", "Weekend"])

            Passenger_Count = st.selectbox("Passenger Count",(1, 2, 3, 4))
            Traffic_Conditions = st.selectbox("Traffic Conditions", ["Low", "Medium", "High"])
            Weather = st.selectbox("Weather", ["Clear", "Rain", "Snow"])

            submitted = st.form_submit_button("Predict")
    
        if submitted:
            payload = {
                "Trip_Distance_km": Trip_Distance_km,
                "Time_of_Day": Time_of_Day,
                "Day_of_Week": Day_of_Week,
                "Passenger_Count": Passenger_Count,
                "Traffic_Conditions": Traffic_Conditions,
                "Weather": Weather,
                "Trip_Duration_Minutes": Trip_Duration_Minutes
            }

            response = httpx.post(f"{URL}/taxi/predict", json=payload)
            result = response.json().get("predicted_price")


            st.success(f"Predicted price: {result:.2f} USD")

            with st.expander("Show details"):
                st.write("### Prediction details")
                st.json(payload)



if __name__ == "__main__":
    main()
