import streamlit as st
from functools import reduce
import operator

st.set_page_config(page_title="Calculator App", page_icon="🧮")

st.title("🧮 Calculator Application")

operation = st.selectbox(
    "Choose an operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)

if operation in ["Addition (+)", "Multiplication (*)"]:
    values_input = st.text_input(
        "Enter values separated by commas",
        placeholder="Example: 10, 20, 30"
    )
else:
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            values = [float(value.strip()) for value in values_input.split(",")]
            st.success(f"Addition of all values: **{sum(values):.2f}**")

        elif operation == "Subtraction (-)":
            st.info(f"{num1} - {num2} = **{num1 - num2:.2f}**")
            st.info(f"{num2} - {num1} = **{num2 - num1:.2f}**")

        elif operation == "Multiplication (*)":
            values = [float(value.strip()) for value in values_input.split(",")]
            result = reduce(operator.mul, values, 1)
            st.success(f"Multiplication of all values: **{result:.2f}**")

        elif operation == "Division (/)":
            if num2 != 0:
                st.success(f"{num1} ÷ {num2} = **{num1 / num2:.2f}**")
            else:
                st.error("Division by zero is not possible.")

    except ValueError:
        st.error("Please enter valid numeric values separated by commas.")