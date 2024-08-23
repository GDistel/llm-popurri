from pydantic import BaseModel

class QueryWebsiteRequest(BaseModel):
    url: str
    question: str

class QuestionAnswerResponse(BaseModel):
    question: str
    answer: str

class QueryWebsiteResponse(BaseModel, QuestionAnswerResponse):
    url: str
