from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import subprocess
import os

app = FastAPI()


# Mount the /static folder
app.mount("/fast_api/static", StaticFiles(directory="fast_api/static"), name="static")


# Set root route to serve the HTML page
@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("fast_api/static/index.html") as f:
        return f.read()


@app.get("/crawl")
def run_books_spider():
    subprocess.run("scrapy crawl books_spider -O books.json".split(), check=True)

    # Check if the file was created
    if not os.path.exists("books.json"):
        return {"error": "Failed to generate books.json"}

    # Return the file as a response
    return FileResponse(
        "books.json", media_type="application/json", filename="books.json"
    )
