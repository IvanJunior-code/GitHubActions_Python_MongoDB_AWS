from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # Adicione esta importação

app = FastAPI()

@app.get("/", response_class=HTMLResponse)  # Use a classe de resposta HTMLResponse
def read_root():
    html_content = """
    <html>
        <head>
            <title>FastAPI Hello World</title>
        </head>
        <body style="text-align: center;">
            <h1>Welcome to FastAPI Hello World!</h1>
            <p>This is a customized Hello World page using FastAPI.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
