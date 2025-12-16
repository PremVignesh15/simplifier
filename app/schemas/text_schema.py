# app/schemas/text_schema.py
from pydantic import BaseModel, Field
from typing import Optional

class SimplifyRequest(BaseModel):
    sentence: str = Field(..., example="The rapid technological advancements significantly transformed various industries.")
    tone: Optional[str] = Field(None, description="Optional: tone to use (e.g., 'casual', 'formal', 'child-friendly').")
    max_tokens: Optional[int] = Field(None, description="Optional: override default max tokens for the model.")
    temperature: Optional[float] = Field(None, description="Optional: override default temperature (0.0-1.0).")

class SimplifyResponse(BaseModel):
    
    simplified: str
    original: str



