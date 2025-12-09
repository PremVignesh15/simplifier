# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.text_schema import SimplifyRequest, SimplifyResponse
from app.services.simplify_service import simplify as simplify_service
from app.config import APP_DEBUG, APP_HOST, APP_PORT, COHERE_MODEL


# Note: When running directly with `uvicorn app.main:app` (from simplifier folder),
# make sure PYTHONPATH includes the project root or run from project root.

app = FastAPI(title="Sentence Simplifier", version="1.0")

# Allow local frontends to access this API during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"status": "ok", "message": "Sentence Simplifier API. POST to /simplify"}

@app.post("/simplify", response_model=SimplifyResponse)
def simplify(request: SimplifyRequest):
    if not request.sentence or request.sentence.strip() == "":
        raise HTTPException(status_code=400, detail="`sentence` must be a non-empty string.")

    try:
        simplified_text = simplify_service(
            sentence=request.sentence,
            tone=request.tone,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return SimplifyResponse(original=request.sentence, simplified=simplified_text, model=COHERE_MODEL)
