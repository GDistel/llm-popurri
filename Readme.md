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

## Postgres connection URI

From within docker you can reference your host computer `localhost` as `host.docker.internal`

For example:
- If you use docker: `postgresql://postgres:postgres@host.docker.internal.docker.internal:5432/test_db`
- Otherwise: `postgresql://postgres:postgres@host.docker.internal:5432/test_db`

Alternatively, if the postgres is running on docker, you can add both to the same network.
