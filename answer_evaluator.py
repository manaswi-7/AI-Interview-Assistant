from google import genai
from config import API_KEY

client = genai.Client(
    api_key=API_KEY
)

def evaluate_answer(question, answer):

    prompt = f"""
    Question:
    {question}

    Answer:
    {answer}

    Evaluate the answer.

    Give:
    - Score /10
    - Strengths
    - Weaknesses
    - Suggestions
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"API Error: {str(e)}"