import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model (1.5 Flash)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Streamlit UI
st.set_page_config(page_title="Customer Support Agent - Gemini", layout="centered")

st.title("🤖 Customer Support GenAI Agent ")
st.write("Ask your BFSI-related queries below (Loan, Credit Cards, Accounts, etc.):")

# User input
user_query = st.text_area("Enter your query here:")

if st.button("Get Response"):
    if user_query.strip() == "":
        st.warning("Please enter a query.")
    else:
        with st.spinner("Generating response..."):
            try:
                prompt = f"You are a helpful customer support agent for banking and insurance sector. Answer this query:\n\n{user_query}"
                response = model.generate_content(prompt)
                st.success("Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
