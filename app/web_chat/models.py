from pydantic import BaseModel

class QueryWebsiteRequest(BaseModel):
    url: str
    question: str

class QueryWebsiteResponse(BaseModel):
    url: str
    question: str
    answer: str
