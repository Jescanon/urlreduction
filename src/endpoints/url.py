from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid

from src.database.sesion import get_db

from src.head.pyndantics import Url

from src.schema.url import Url as UrlSchema
router = APIRouter()

@router.post("/url")
async def url(urls: Url, db:  AsyncSession = Depends(get_db)):
    urlss = str(urls.url)

    info = await db.scalars(select(UrlSchema).where(UrlSchema.url == urlss))

    url = info.first()
    if url:
        return f"http://127.0.0.1:8082/{url.sketch}"

    stroka = uuid.uuid4().hex[:6]

    model = UrlSchema(sketch=stroka, url=urlss)

    db.add(model)
    await db.commit()
    return f"http://127.0.0.1:8082/{model.sketch}"


