# Customer Support GenAI Agent (Streamlit Version)

## About
This is a simple Customer Support AI agent for BFSI (Banking, Financial Services, and Insurance) sector built using Python and Streamlit.  
It uses OpenAI's GPT model to answer user queries.

## Features
- Simple Streamlit Web UI
- OpenAI GPT-based responses
- Focused on BFSI customer support queries

## Local Setup Instructions

### 1. Clone / Download the project
```
git clone [repo link or download ZIP]
cd customer_support_agent_streamlit
```

### 2. Install required packages
```
pip install -r requirements.txt
```

### 3. Add your OpenAI API key
- Create a file named `.env`
- Paste this inside:
```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
```

### 4. Run the app
```
streamlit run app.py
```

### 5. Open your browser
Visit:  
```
http://localhost:8501
```

## Hosting (After Local Testing)
- Streamlit Cloud (Free)
- Render.com
- Railway.app

## License
MIT