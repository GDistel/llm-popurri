# LLM popurri

API for just a mix of LLM related functionality.
An API key for OpenAI is required. And you will also need an API key for Langsmith: https://smith.langchain.com/ (it's free).
See the .env.template and set those up in a `.env` file.

## Spin up with Docker

As easy as `docker compose up` (mind to have a compliant `.env` file)

## Spin up with FastAPI

- Create virtual env `python3 -m venv venv`
- Install dependencies with `pip install -r requirements.txt`
- Create the `.env` file
- Start the app with `fastapi dev app/main.py` (or `fastapi run app/main.py` for production)

## Usage

See docs at `${baseURL}/docs`
