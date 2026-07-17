from fastapi import FastAPI

app = FastAPI(
    title="AgentLens API",
    description="AI Reliability & Evaluation Platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "project": "AgentLens",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }