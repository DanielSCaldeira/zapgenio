# backend/dependencies/empresa_dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.empresa_service import EmpresaService
from backend.database.connection import get_db

async def get_empresa_service(db: AsyncSession = Depends(get_db)) -> EmpresaService:
    return EmpresaService(db)
