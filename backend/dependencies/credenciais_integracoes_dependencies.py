from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database.connection import get_db
from backend.services.credencias_integracoes_service import CredenciaisIntegracoesService

# Dependência para injetar o serviço de CredenciaisIntegracoes
async def get_credenciais_integracoes_service(db: AsyncSession = Depends(get_db)) -> CredenciaisIntegracoesService:
    return CredenciaisIntegracoesService(db)
