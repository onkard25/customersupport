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
                prompt = f"""
You are a highly trained and professional Customer Support Assistant for the Banking, Financial Services, and Insurance (BFSI) sector.

Your task is to respond to customer queries in a helpful, structured, and polite manner.

User Query:
{user_query}

Guidelines for your response:
- Clearly understand the intent of the query.
- Use numbered lists or bullet points where applicable.
- Provide accurate, elaborative explanations in simple language.
- If needed, explain financial terms in layman's terms.
- If the query is vague or incomplete, suggest clarifying questions.
- End with a friendly tip or polite closing line.
- Try to keep the response under 600 words for readability.

Now respond to the user's question below:
"""

                response = model.generate_content(prompt)
                st.success("Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
