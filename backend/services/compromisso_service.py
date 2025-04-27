
from models.compromisso import Compromisso
from services.base import BaseService
from sqlalchemy.orm import Session

class CompromissoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(Compromisso)
        self.db = db 
    
