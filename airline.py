import numpy as np
import pandas as pd
import streamlit as st
from joblib import load

# Configure the page layout
st.set_page_config(layout="wide")

# App title
st.title(" :red[Airline Customer Satisfaction Prediction]")

# Define dictionaries for mapping strings to integers
gender_dict = {'Male': 0, 'Female': 1}
customer_type_dict = {'First-time': 0, 'Returning': 1}
travel_type_dict = {'Business': 0, 'Personal': 1}
class_dict = {'Business': 0, 'Economy': 1, 'Economy Plus': 2}

# Define options for the select boxes
gender_values = ['Male', 'Female']
customer_type_values = ['First-time', 'Returning']
travel_type_values = ['Business', 'Personal']
class_values = ['Business', 'Economy', 'Economy Plus']

st.write(' :white[Fill the below details to predict customer satisfaction]')

# Create a form for user input
with st.form('SatisfactionPrediction'):
    col1, col2 = st.columns([0.5, 0.5])

    with col1:
        gender = st.selectbox(label='Gender', options=gender_values)
        age = st.number_input(label='Age', min_value=0, max_value=100, value=30)
        customer_type = st.selectbox(label='Customer Type', options=customer_type_values)
        travel_type = st.selectbox(label='Type of Travel', options=travel_type_values)
        travel_class = st.selectbox(label='Class', options=class_values)

    with col2:
        flight_distance = st.number_input(label='Flight Distance', min_value=0, max_value=5000, value=1000)
        departure_delay = st.number_input(label='Departure Delay (minutes)', min_value=0, max_value=100, value=0)
        arrival_delay = st.number_input(label='Arrival Delay (minutes)', min_value=0, max_value=100, value=0)

        # Add more input fields as necessary based on the model's requirements

        button = st.form_submit_button(label='SUBMIT')

# Process user input and make predictions
if button:
    # Convert user inputs to the appropriate format
    gender_int = gender_dict.get(gender)
    customer_type_int = customer_type_dict.get(customer_type)
    travel_type_int = travel_type_dict.get(travel_type)
    travel_class_int = class_dict.get(travel_class)

    # Combine inputs into a NumPy array
    input_data = np.array([[gender_int, age, customer_type_int, travel_type_int, travel_class_int, flight_distance, departure_delay, arrival_delay]])

    # Load the saved model
    file_path = 'airline_satisfaction_model.pkl'  # Adjust the file path as per your saved model
    loaded_model = load(file_path)

    # Make predictions
    y_pred = loaded_model.predict(input_data)
    predicted_satisfaction = 'Satisfied' if y_pred[0] == 1 else 'Neutral or Dissatisfied'

    # Display the prediction
    st.header(f'Predicted Customer Satisfaction: {predicted_satisfaction}')
