from pydantic import BaseModel

class TranslationRequest(BaseModel):
    language: str
    text: str

class TranslationResponse(BaseModel):
    language: str
    original_text: str
    translated_text: str