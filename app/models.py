from pydantic import BaseModel

class TranslationRequest(BaseModel):
    language: str
    text: str

class TranslationResponse(BaseModel):
    language: str
    original_text: str
    translated_text: str

class QueryWebsiteRequest(BaseModel):
    url: str
    question: str

class QuestionAnswerResponse(BaseModel):
    question: str
    answer: str

class QueryWebsiteResponse(QuestionAnswerResponse):
    url: str
