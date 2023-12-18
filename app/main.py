from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from pydantic import BaseSettings

app = FastAPI()

class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"

settings = Settings()

@app.get("/")
def read_root():
    html_content = """
    <html>
        <head>
            <title>FastAPI Hello World</title>
        </head>
        <body style="text-align: center; padding: 50px;">
            <h1>Welcome to FastAPI Hello World!</h1>
            <p>This is a customized Hello World page using FastAPI.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
