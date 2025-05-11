from backend.models.credenciais_integracoes import CredenciaisIntegracoes
from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession

class CredenciaisIntegracoesService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(CredenciaisIntegracoes, db)
        self.db = db
