from fastapi import FastAPI, HTTPException
from app.translations.models import TranslationRequest, TranslationResponse
from app.translations.llm import translate as llm_translate
from app.web_chat.llm import answer_question
from app.web_chat.models import QueryWebsiteRequest, QueryWebsiteResponse

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)