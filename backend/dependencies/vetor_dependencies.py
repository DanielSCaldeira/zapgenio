# backend/dependencies/vetor_dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.vetor_service import VetorService
from backend.database.connection import get_db

async def get_vetor_service(db: AsyncSession = Depends(get_db)) -> VetorService:
    return VetorService(db)
