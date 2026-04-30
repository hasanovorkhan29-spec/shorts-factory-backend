from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

class RequestModel(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/generate-video")
async def generate_video(req: RequestModel):
    topic = req.topic

    # Script
    script = f"{topic} haqqında motivasiyaedici qısa video. Uğur üçün çalış, dayanma!"

    # ElevenLabs voice
    voice_api = os.getenv("ELEVEN_API_KEY")
    audio_file = "voice.mp3"

    if voice_api:
        url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"
        headers = {
            "xi-api-key": voice_api,
            "Content-Type": "application/json"
        }
        data = {
            "text": script,
            "model_id": "eleven_monolingual_v1"
        }
        r = requests.post(url, json=data, headers=headers)
        with open(audio_file, "wb") as f:
            f.write(r.content)

    return {
        "status": "ok",
        "topic": topic,
        "script": script,
        "message": "Video hazırlanır..."
    }
