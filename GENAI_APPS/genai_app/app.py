from openai import OpenAI
import streamlit as st

# Load API key from a file
with open(r"D:\DATA_SCIENCE_INTERNSHIP\GenAI_app-main\GenAI_app-main\GENAI_APPS\app_keys\openai_key.txt") as f:
    key = f.read().strip()  # Strip whitespace and newline characters

# Create OpenAI client
client = OpenAI(api_key=key)

st.title("AI MCQ Generator")
st.subheader("soon to be a Billion Dollar App Idea")

# Input prompt from the user
prompt = st.text_input("Enter the Data Science Topic")

if st.button("Generate"):
    st.balloons()
    # Check if there's a prompt provided before making the API call
    if prompt:
        response = client.completions.create(
            model="davinci",  # Using the davinci model
            prompt="YOU are helpful AI Assistant\n\nGiven the topic of Data Science, you will generate 3 MCQ questions and answers for a test.\n\n" + prompt,
            max_tokens=150  # Adjust as needed
        )
        # Display the generated content
        st.write(response.choices[0].text.strip())
    else:
        st.write("Please provide a Data Science topic.")
