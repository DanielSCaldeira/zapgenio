from services.base import BaseService
from sqlalchemy.orm import Session
from models.usuario import Usuario

class UsuarioService(BaseService):
    
    def __init__(self, db: Session):
        super().__init__(Usuario) 
        self.db = db 

  
