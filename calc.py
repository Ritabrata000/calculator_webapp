import streamlit as st
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

def calculator():
    st.title("Simple Calculator by Ritabrata")

    # Input for the first number
    num1 = st.number_input("Enter the first number:", value=0)

    # Input for the second number
    num2 = st.number_input("Enter the second number:", value=0)

    # Operation selection
    operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

    result = 0.0

    # Perform the selected operation
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero. Please enter a non-zero value for the second number.")

    # Display the result
    st.success(f"Result: {result}")

if __name__ == "__main__":
    st.markdown(hide_st_style, unsafe_allow_html=True)
    calculator()
