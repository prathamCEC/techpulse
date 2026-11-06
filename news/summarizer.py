
import json
import time

from google import genai
from google.genai import types

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    GEMINI_FALLBACK_MODEL
)


client = genai.Client(api_key=GEMINI_API_KEY)

RETRY_ATTEMPTS = 2
RETRY_DELAY = 2

RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


def generate_summary(article, model):

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

    response = client.models.generate_content(
        model=model,
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

    if not isinstance(result, dict):
        raise ValueError("Gemini returned an invalid JSON object")

    if not all(
        isinstance(result.get(field), str) and result[field].strip()
        for field in required_fields
    ):
        raise ValueError("Gemini returned incomplete JSON")

    return result


def is_retryable_error(error):

    status_code = getattr(error, "code", None)

    if status_code is None:
        status_code = getattr(error, "status_code", None)

    if status_code is None:
        response = getattr(error, "response", None)
        status_code = getattr(response, "status_code", None)

    return status_code in RETRYABLE_STATUS_CODES


def summarize_article(article):

    models = [GEMINI_MODEL]

    if GEMINI_FALLBACK_MODEL != GEMINI_MODEL:
        models.append(GEMINI_FALLBACK_MODEL)

    for model in models:

        print(f"[GEMINI] Using model: {model}", flush=True)

        for attempt in range(RETRY_ATTEMPTS):

            try:

                result = generate_summary(article, model)

                print(
                    f"[GEMINI] Successfully summarized using {model}",
                    flush=True
                )

                return result

            except Exception as error:

                if not is_retryable_error(error):
                    print(
                        f"[GEMINI] Non-retryable error with {model}: {error}",
                        flush=True
                    )
                    break

                if attempt < RETRY_ATTEMPTS - 1:

                    delay = RETRY_DELAY * (2 ** attempt)

                    print(
                        f"[GEMINI] Temporary error with {model}. "
                        f"Retrying in {delay}s: {error}",
                        flush=True
                    )

                    time.sleep(delay)

                else:
                    print(
                        f"[GEMINI] {model} failed after "
                        f"{RETRY_ATTEMPTS} attempts.",
                        flush=True
                    )

        if model != models[-1]:
            print(
                f"[GEMINI] Switching to fallback model: {models[1]}",
                flush=True
            )

    print("[GEMINI] All available models failed.", flush=True)

    return None
