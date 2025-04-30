# backend/dependencies/lista_pergunta_resposta_dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.lista_pergunta_resposta_service import ListaPerguntaRespostaService
from backend.database.connection import get_db

async def get_lista_pergunta_resposta_service(db: AsyncSession = Depends(get_db)) -> ListaPerguntaRespostaService:
    return ListaPerguntaRespostaService(db)
