import streamlit as st

# Conversion factors (Dictionary approach)
conversion_factors = {
    "Length": {"meters": 1, "feet": 3.28084, "miles": 0.000621371, "kilometers": 0.001},
    "Weight": {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274},
}

# Streamlit UI
st.title("Simple Unit Converter ")

category = st.selectbox("Choose category:", conversion_factors.keys())
from_unit = st.selectbox("Convert from:", conversion_factors[category].keys())
to_unit = st.selectbox("Convert to:", conversion_factors[category].keys())
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

# Conversion logic
if st.button("Convert"):
    result = value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
    st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
