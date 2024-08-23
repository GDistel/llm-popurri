# LLM tutorial

## Spin up with Docker

As easy as `docker compose up` (mind to have a compliant `.env` file)

## Spin up with FastAPI

- Create virtual env `python3 -m venv venv`
- Install dependencies with `pip install -r requirements.txt`
- Create `.env` file
- Start the app with `fastapi dev app/main.py` (or `fastapi run app/main.py` for production)

## Usage

See docs at `${baseURL}/docs`