from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request modeli
class RequestModel(BaseModel):
    topic: str

# Test endpoint
@app.get("/")
def home():
    return {"status": "ok"}

# Video generate endpoint
@app.post("/generate-video")
async def generate_video(req: RequestModel):
    topic = req.topic

    # Demo response (sonra real video ilə əvəz edəcəyik)
    return {
        "success": True,
        "video_url": "https://example.com/video.mp4",
        "title": f"{topic} haqqında video",
        "description": f"Bu video {topic} mövzusunda hazırlanıb.",
        "message": f"Video hazırlandı: {topic}"
    }
