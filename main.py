from httplib2 import Response
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "daniel"}

@app.get("/status", status_code=204)
async def root():
    return

@app.get("/info", status_code=200)
async def root():
    server_url = "localhost:8000/info"
    return {"url": f"{server_url}"}

@app.delete("/security", status_code=401)
async def root():
    return