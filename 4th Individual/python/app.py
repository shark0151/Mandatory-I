from fastapi import FastAPI
import uvicorn
import requests
from datetime import datetime

app = FastAPI()
url = "http://127.0.0.1:8081/time"


@app.get("/time")
def _():
    return {"time": datetime.now().timestamp()}


@app.get("/time/NodeServer")
def _():
    response = requests.request("GET", url)
    print(response.text)
    return {response.text}


uvicorn.run(app, host="127.0.0.1", port=8080)
