
from backend.models.empresa import Empresa
from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession

class EmpresaService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(Empresa, db)  # Passa a classe Empresa para a classe base
        self.db = db 





