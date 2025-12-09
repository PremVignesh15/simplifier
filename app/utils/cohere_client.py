# app/utils/cohere_client.py

import cohere
from app.config import (
    COHERE_API_KEY,
    COHERE_MODEL,
    COHERE_MAX_TOKENS,
    COHERE_TEMPERATURE
)

_client = None


def get_client():
    """
    Create the Cohere client once and reuse it.
    """
    global _client
    if _client is None:
        if not COHERE_API_KEY:
            raise RuntimeError("COHERE_API_KEY is missing in .env")
        _client = cohere.Client(COHERE_API_KEY)
    return _client


def generate_simplification(
    prompt: str,
    max_tokens: int = None,
    temperature: float = None,
    model: str = None
) -> str:

    client = get_client()

    _model = model or COHERE_MODEL
    _max_tokens = max_tokens or COHERE_MAX_TOKENS
    _temperature = COHERE_TEMPERATURE if temperature is None else temperature

    try:
        response = client.chat(
            model=_model,
            message=prompt,
            max_tokens=_max_tokens,
            temperature=_temperature
        )
    except Exception as e:
        raise RuntimeError(f"Cohere API error: {e}")

    # New-style chat responses contain 'text'
    if not hasattr(response, "text"):
        raise RuntimeError("Cohere returned no 'text' field.")

    return response.text.strip()
