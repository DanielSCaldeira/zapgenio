from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models.usuario import Usuario

class UsuarioService(BaseService):    
    def __init__(self, db: AsyncSession):
        super().__init__(Usuario, db) 
        self.db = db 

  
