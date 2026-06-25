
from google import genai
from config import API_KEY
client = genai.Client(
    api_key=API_KEY
)

def generate_questions(resume_summary, category):

    prompt = f"""
    Candidate Profile:

    {resume_summary}

    Generate 10 {category} interview questions.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text