# Import streamlit library
import pandas as pd
import streamlit as st
import json
import requests
import openai
import os

# Set the title of the app
st.title("Solomon")

# Create a file uploader widget for file input
file_input = st.sidebar.file_uploader("Upload a csv file")

# Read the csv file into a pandas dataframe using pandas.read_csv()
if file_input is not None:
    df = pd.read_csv(file_input)

    # Display the dataframe in the sidebar using streamlit.sidebar.dataframe()
    st.sidebar.dataframe(df)

# Create a text input widget for user input
user_input = st.text_input("How do you want to transform your data?")

# Display the user input
st.write(f"You entered: {user_input}")



st.code("""
df = pd.read_csv("data.csv")
st.dataframe(df)
""", language="python")

