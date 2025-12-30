from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FutureGuard AI Backend")

# CORS (Vercel frontend ke liye zaroori)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "FutureGuard AI Backend is live"
    }

@app.post("/analyze")
def analyze(data: dict):
    user_input = data.get("input", "")

    # Temporary AI logic (baad me OpenAI add karenge)
    return {
        "risk_level": "Low",
        "summary": f"Analysis received for: {user_input}",
        "action": "No immediate action required"
    }
