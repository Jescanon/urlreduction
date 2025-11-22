from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from src.endpoints.url import router

from src.schema.url import Url as UrlSchema

from src.database.sesion import get_db

app = FastAPI()

app.include_router(router)



@app.get("/{ids}")
async def root(ids: str, db: AsyncSession = Depends(get_db)):
    info = await db.scalars(select(UrlSchema).where(UrlSchema.sketch == ids))

    url = info.first()

    if url is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return RedirectResponse(url=url.url)
