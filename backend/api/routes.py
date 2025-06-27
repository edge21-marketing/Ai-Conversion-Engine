from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/health")
async def health_check():
    return {"status": "ok", "detail": "API running smoothly"}
