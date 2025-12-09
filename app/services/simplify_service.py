# app/services/simplify_service.py
from typing import Optional
from app.utils.cohere_client import generate_simplification
from app.config import COHERE_MODEL


def build_prompt(sentence: str, tone: Optional[str] = None) -> str:
    """
    Construct a strict prompt that forces the model to output ONLY the simplified sentence.
    """

    base = (
        "Simplify the sentence below.\n"
        "Rules:\n"
        "- Output ONLY the simplified sentence.\n"
        "- Do NOT say anything before or after it.\n"
        "- Do NOT add quotes.\n"
        "- Do NOT explain.\n"
        "- Do NOT start with phrases like 'Sure', 'Here is', etc.\n"
        "- Preserve the meaning but use simpler language.\n"
    )

    if tone:
        base += f"- Tone: {tone}\n"

    base += f"\nSentence: {sentence}\n\nSimplified sentence:"
    return base


def simplify(sentence: str, tone: Optional[str] = None, max_tokens: Optional[int] = None, temperature: Optional[float] = None) -> str:
    prompt = build_prompt(sentence, tone)
    simplified = generate_simplification(prompt=prompt, max_tokens=max_tokens, temperature=temperature, model=COHERE_MODEL)
    return simplified
