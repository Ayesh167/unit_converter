import streamlit as st

# Function to convert between units
def convert_units(value, from_unit, to_unit):
    # Length units conversion (example)
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084
    }
    
    # Check if the units are valid
    if from_unit not in length_units or to_unit not in length_units:
        return "Invalid units"
    
    # Convert the value to meters first
    value_in_meters = value * length_units[from_unit]
    
    # Convert from meters to the target unit
    return value_in_meters / length_units[to_unit]

# Streamlit user interface
st.title('Unit Converter')

st.write("### Convert between different units of length")

# User inputs
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From unit:", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet"])
to_unit = st.selectbox("To unit:", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet"])

# Perform conversion when button is pressed
if st.button('Convert'):
    result = convert_units(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
