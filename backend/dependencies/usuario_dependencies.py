# backend/dependencies/usuario_dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.usuario_service import UsuarioService
from backend.database.connection import get_db

async def get_usuario_service(db: AsyncSession = Depends(get_db)) -> UsuarioService:
    return UsuarioService(db)
