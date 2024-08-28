from fastapi import FastAPI, Form, HTTPException, File, UploadFile
from app.db_ask import ask_question_to_db
from app.models import QueryDBRequest, TranslationRequest, TranslationResponse, QueryWebsiteRequest, QueryWebsiteResponse, QuestionAnswerResponse
from app.pdf_questions import answer_question_with_pdf, create_path_for_file
from app.translations import translate as llm_translate
from app.web_chat import answer_question

app = FastAPI()

@app.post("/translate")
async def translate(translation_request: TranslationRequest) -> TranslationResponse:
    language = translation_request.language
    text = translation_request.text
    translation = await llm_translate(text, language)
    return {
        "language": language,
        "original_text": text,
        "translated_text": translation
    }

@app.post("/query_wikipedia")
async def query_wikipedia(query_website_request: QueryWebsiteRequest) -> QueryWebsiteResponse:

    url = query_website_request.url
    if ('wikipedia.org/wiki' not in url):
        raise HTTPException(status_code=400, detail="Invalid URL. Only Wikipedia URLs are supported.")

    question = query_website_request.question
    answer = await answer_question(url, question)

    return {
        "url": url,
        "question": question,
        "answer": answer
    }

@app.post("/ask_pdf")
async def upload_pdf(file: UploadFile = File(...), question: str = Form(...)) -> QuestionAnswerResponse:
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only pdf files allowed")

    content = await file.read()
    file_path = create_path_for_file(file.filename)

    with open(file_path, "wb") as f:
        f.write(content)

    answer = await answer_question_with_pdf(question, file_path)

    return {
        "question": question,
        "answer": answer
    }

@app.post("/ask_db")
async def ask_db(db_query_request: QueryDBRequest):
    question = db_query_request.question
    response = ask_question_to_db(question)
    return {
        "response": response,
    }