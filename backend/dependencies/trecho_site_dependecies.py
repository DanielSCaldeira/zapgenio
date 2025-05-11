# backend/dependencies/trecho_site_dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database.connection import get_db
from backend.services.trech_site_service import TrechoSiteService

async def get_trecho_site_service(db: AsyncSession = Depends(get_db)) -> TrechoSiteService:
    return TrechoSiteService(db)
