from google import genai
from config import API_KEY

client = genai.Client(
    api_key=API_KEY
)


def check_ats_score(resume_text):

    prompt = f"""
    Analyze this resume.

    Provide:

    1. ATS Score out of 100
    2. Missing Keywords
    3. Formatting Issues
    4. Strengths
    5. Suggestions for Improvement

    Resume:
    {resume_text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text