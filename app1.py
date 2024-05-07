
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image


pickle_in = open("xgb_model.pkl","rb")
classifier=pickle.load(pickle_in)


def price_prediction(trip_miles, trip_time, pickup_hour, pickup_day):
    data = {
    'trip_miles': trip_miles,
    'trip_time': trip_time,
    'pickup_hour': pickup_hour,
    'pickup_day': pickup_day
         }

    # Create a DataFrame
    input_data = pd.DataFrame([data])
    print(input_data)
    prediction=classifier.predict(input_data)
    print(prediction)
    return prediction



def main():

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">UBER Price Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    trip_miles = st.number_input("Enter trip miles", min_value=0.0)
    trip_time = st.number_input("Enter trip time", min_value=0.0)
    pickup_hour = st.number_input("Enter pickup hour", min_value=0, max_value=23, step=1)
    pickup_day = st.number_input("Enter pickup day", min_value=1, max_value=31, step=1)
    

    # Convert inputs to appropriate numeric types   
    trip_miles = float(trip_miles)
    trip_time = int(trip_time)
    pickup_hour = int(pickup_hour)
    pickup_day = int(pickup_day)
 


    result=""
    if st.button("Predict"):
        result=price_prediction(trip_miles, trip_time, pickup_hour, pickup_day)
    st.success(f'The predicted trip price is: ${result}')


if __name__=='__main__':
    main()
    
    
    