from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Cho phép frontend (Vercel) gọi API mà không bị lỗi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Sau này có thể siết lại ["https://ve-mini-frontend.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    text: str

@app.get("/")
def index():
    return {"message": "Backend is running!"}

@app.post("/generate-video")
def generate_video(req: GenerateRequest):
    return {
        "status": "ok",
        "input_text": req.text,
        "video_url": "https://example.com/fake-video.mp4"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
