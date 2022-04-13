from httplib2 import Response
from fastapi import FastAPI
from starlette.responses import FileResponse


app = FastAPI()


@app.get("/")
async def read_index():
    return FileResponse('pagina.html')
