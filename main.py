import json
import os

from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse

app = FastAPI()

@app.get("/images/{filename}")
async def get_image(filename: str):
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images", filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Image not found")
    
    return FileResponse(filepath)
    