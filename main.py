# external/main.py

import sys
import os

# Add 'src' folder to Python path so we can import from it
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from fastapi import FastAPI
from src.api.routes.research import router as research_router

app = FastAPI(
    title="Personal Research Assistant API",
    description="Fetch and summarize academic papers using agentic AI.",
    version="0.1.0"
)

# Register routes
app.include_router(research_router, prefix="/api/v1/research")

@app.on_event("startup")
async def startup_event():
    print("\n🔍 Registered Routes:")
    for route in app.routes:
        if hasattr(route, "path"):
            print(f" - {route.methods} {route.path}")
    print()
@app.get("/")
def read_root():
    return {"message": "Welcome to the Personal Research Assistant API"}

# Run the app if this file is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)