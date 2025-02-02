#!/usr/bin/env python
import sys
import warnings
from crew import AiVehicleCrew


from datetime import datetime

from crew import AiVehicleCrew
import streamlit as st



warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Add a header with blue font
st.markdown("<h1 style='color: blue;'>Choose Your Vehicle</h1>", unsafe_allow_html=True)
# Define the options for the multi-select box
options = ["SUV", "SEDAN", "COUPE", "VAN", "UTILITY VEHICLE"]

# Create a multi-select box
user_input = st.multiselect("Please select the vehicle type  you want to buy:", options)

def run():
    """
    Run the crew.
    """
    # Convert the list of selected options to a comma-separated string
    user_input_str = ", ".join(user_input)
    
    inputs = {
        'input': user_input_str,
        'input_str': user_input_str 
    }
  ##  AiVehicleCrew().crew().kickoff(inputs=inputs)

    
   

# Create a submit button
if st.button("Submit"):
    st.write("Vehicle Market Analysis workflow kicked off successfully!")
    run()


     
run()