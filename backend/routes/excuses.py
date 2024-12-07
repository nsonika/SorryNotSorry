from fastapi import APIRouter, HTTPException
from schemas.excuse_schema import ExcuseRequest, ExcuseResponse
from services.ai_generator import generate_excuse

router = APIRouter()

@router.post("/generate", response_model=ExcuseResponse)
def generate_excuse_route(request: ExcuseRequest):
    try:
        excuse = generate_excuse(request.category, request.humor_level, request.custom_context)
        return {"excuse": excuse}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
