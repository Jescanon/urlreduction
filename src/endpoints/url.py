from fastapi import APIRouter

router = APIRouter()

@router.get("/url")
async def url():
    pass