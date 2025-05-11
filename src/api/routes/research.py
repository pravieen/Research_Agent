# src/api/routes/research.py
from fastapi import APIRouter, HTTPException
from src.schemas.schemas import ResearchResponse, ResearchRequest

# Agent-related imports will go here later
from src.agents.research_agent import ResearchAgent

router = APIRouter()
print("22222 - research.py loaded")


@router.post("/summarize", response_model=ResearchResponse)
def summarize_research(request: ResearchRequest):
    print("✅ Endpoint reached: /summarize")
    try:
        agent = ResearchAgent()
        result = agent.run(request.query, request.max_results)

        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")