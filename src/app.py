import streamlit as st
from datetime import datetime
import numpy as np
import pandas as pd
from Test24H import predict_for_date
import numpy as np

# # Function to simulate prediction (replace this with your actual model prediction function)
# def predict_for_date(date):
#     # Here we simulate generating a random prediction for simplicity
#     return np.random.rand(24)

# Title of the app
st.title('24-Hour Trip Prediction')

# User input for the dateclea
user_input_date = st.date_input("Choose a date for prediction:", min_value=datetime(2017, 1, 1), max_value=datetime(2017, 12, 31))

# Convert user input into datetime (if needed, depending on your predict function)
date_to_predict = pd.to_datetime(user_input_date)

# Button to make prediction
if st.button('Predict Trips'):
    # Assuming you have a function that can take a date and return a list of 24 predictions
    predictions = predict_for_date(date_to_predict)
    
    # Display predictions
    st.write(f"Predictions for {user_input_date}:")
    st.line_chart(predictions)  # Displaying the predictions as a line chart

# Running the app
# To run the app, save this script and run `streamlit run app.py` from your command line.
