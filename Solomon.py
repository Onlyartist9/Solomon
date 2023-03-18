# Import streamlit library
import pandas as pd
import streamlit as st
import openai
import os

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set the title of the app
st.title("Data Transformer")

# Create a file uploader widget for file input
file_input = st.sidebar.file_uploader("Upload a csv file")

# Read the csv file into a pandas dataframe using pandas.read_csv()
if file_input is not None:
    df = pd.read_csv(file_input)

    md_table = df.head().to_markdown()

    # Create a prompt for the AI model using natural language and code snippets
    systemprompt = f"""
                # Python 3
                This is a dataframe:

                {md_table}

                You are a helpful pair coding assistant that converts Natural Language queries to pandas code regarding transformations on a dataframe.
                You'll provide responses in the format: [Code] <Done>
                None of your answers should be in Natural Language.

                For example:
                User: drop columns A and B
                You: df.drop([‘A’, ‘B’], axis=1, inplace=True) <Done>

                User: fill missing values with zero
                You: df.fillna(0) <Done>

                User: group by column E and calculate the mean of column F
                You: df.groupby(‘E’)[‘F’].mean() <Done>

                You just need to provide a one line response.
                """

    # Display the dataframe in the sidebar using streamlit.sidebar.dataframe()
    st.sidebar.dataframe(df)

else:
    st.error("Please input a csv file before handling any tasks", icon="🚨")

response = ""

# Create a text input widget for user input
user_input = st.text_input("How do you want to transform your data?")
button = st.button("Transform")

if user_input != "":

    response = openai.Completion.create(model="code-davinci-002", 
    prompt=systemprompt +"\n\nUser" + user_input, 
    temperature=0, 
    max_tokens=256,
    stop="<Done>")

    output = response["choices"][0]["text"]
    pandas_code = output.split(":")[1]

    # Code display
    st.subheader("Generated Code")
    st.code(pandas_code, language="python")

    st.subheader("Your transformed data")
    transformed = eval(pandas_code)

    st.dataframe(transformed)

    def convert_df(transformed):
        return transformed.to_csv(index=True).encode('utf-8')

    csv = convert_df(transformed)

    # Display download button
    st.download_button(
        label="Press to Download",
        data=csv,
        file_name="file.csv",
        mime="text/csv",
        key='download-csv'
    )
    
else:
     st.error("Please describe how you want to transform your data before hitting transform.", icon="🚨")


