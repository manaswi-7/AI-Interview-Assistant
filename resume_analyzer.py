from google import genai
import streamlit as st

# Get API key from Streamlit secrets (Cloud-safe)
API_KEY = st.secrets["API_KEY"]

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def analyze_resume(resume_text):
    """
    Analyze resume text using Gemini AI and extract key information.
    """

    if not resume_text:
        return "No resume text provided."

    prompt = f"""
You are an expert resume analyzer and technical recruiter.

Analyze the resume below and extract the following clearly:

1. Skills
2. Projects
3. Technologies used
4. Certifications (if any)
5. Summary of candidate profile (2-3 lines)

Resume:
{resume_text}

Return output in a clean structured format.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error while analyzing resume: {str(e)}"