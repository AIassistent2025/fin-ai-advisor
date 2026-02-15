from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.services.ai_service import AIService

router = APIRouter()
ai_service = AIService()

class ReportRequest(BaseModel):
    symbols: List[str]
    timeframe: str = "1mo"
    focus_area: Optional[str] = "growth"

@router.post("/generate-report")
async def generate_report(request: ReportRequest):
    try:
        report = await ai_service.generate_financial_report(
            symbols=request.symbols,
            timeframe=request.timeframe,
            focus_area=request.focus_area
        )
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
