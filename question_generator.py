from google import genai
import streamlit as st

# Secure API key from Streamlit Secrets
API_KEY = st.secrets["API_KEY"]

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def generate_questions(resume_summary, category):
    """
    Generate interview questions based on resume summary and category.
    """

    if not resume_summary:
        return "Resume summary is empty."

    prompt = f"""
You are an expert technical interviewer.

Candidate Profile:
{resume_summary}

Generate 10 {category} interview questions.

Rules:
- Questions should match the candidate's skill level
- Mix of easy, medium, and hard
- Focus on real interview scenarios
- Avoid repeated or generic questions
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"API Error: {str(e)}"