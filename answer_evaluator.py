from google import genai
import streamlit as st

# Get API key securely from Streamlit secrets
API_KEY = st.secrets["API_KEY"]

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def evaluate_answer(question, answer):
    """
    Evaluate a candidate's interview answer using Gemini AI.
    """

    if not question or not answer:
        return "Question or Answer missing."

    prompt = f"""
You are an expert technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and provide:

- Score out of 10
- Strengths
- Weaknesses
- Suggestions for improvement

Give a clear, structured response.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"API Error: {str(e)}"