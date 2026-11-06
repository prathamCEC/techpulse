import json

from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL


client = genai.Client(api_key=GEMINI_API_KEY)


def summarize_article(article):

    prompt = f"""
    You are TechPulse, an intelligent technology news analyst.

    Analyze the following news article.

    TITLE:
    {article.get('title')}

    DESCRIPTION:
    {article.get('description')}

    CATEGORY:
    {article.get('category', 'General Technology')}

    Your task is to generate:

    1. summary:
       Explain what happened in 2-3 concise sentences.

    2. why_it_matters:
       Explain why this development matters to the technology industry.

    3. key_takeaway:
       Provide one important insight for technology enthusiasts
       and software developers.

    RULES:
    - Be objective and informative.
    - Avoid unnecessary technical jargon.
    - Do not invent facts.
    - Use only the information provided.
    - Clearly mention when information is insufficient.
    - Return valid JSON only.
    """

    try:

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.3
            )
        )

        result = json.loads(response.text)

        required_fields = [
            "summary",
            "why_it_matters",
            "key_takeaway"
        ]

        if not all(field in result for field in required_fields):
            raise ValueError("Gemini returned incomplete JSON")

        return result

    except Exception as error:

        print(f"Gemini summarization error: {error}")
        return None
