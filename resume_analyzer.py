from google import genai
from config import API_KEY

client = genai.Client(
    api_key=API_KEY
)
def analyze_resume(resume_text):

    prompt = f"""
    Analyze this resume.

    Extract:
    - Skills
    - Projects
    - Technologies
    - Certifications

    Resume:
    {resume_text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text