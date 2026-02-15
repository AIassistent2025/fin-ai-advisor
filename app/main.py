from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI(
    title="AI-Driven Financial Advisor",
    description="Automated financial insights and portfolio optimization using LLMs.",
    version="0.1.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "Welcome to the AI-Driven Financial Advisor API",
        "status": "active",
        "documentation": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
