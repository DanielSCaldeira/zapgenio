# backend/dependencies/pergunta_resposta_dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.pergunta_resposta_service import PerguntaRespostaService
from backend.database.connection import get_db

async def get_pergunta_resposta_service(db: AsyncSession = Depends(get_db)) -> PerguntaRespostaService:
    return PerguntaRespostaService(db)
