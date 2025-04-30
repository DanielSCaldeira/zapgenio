# backend/dependencies/compromisso_dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.compromisso_service import CompromissoService
from backend.database.connection import get_db

async def get_compromisso_service(db: AsyncSession = Depends(get_db)) -> CompromissoService:
    return CompromissoService(db)
