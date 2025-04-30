
from backend.models.compromisso import Compromisso
from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession

class CompromissoService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(Compromisso)
        self.db = db 
    
