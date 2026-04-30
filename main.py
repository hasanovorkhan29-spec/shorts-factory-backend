from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/generate-video")
async def generate_video(req: Request):
    topic = req.topic
    
    return {
        "status": "ok",
        "message": f"Video generation started for: {topic}"
    }
