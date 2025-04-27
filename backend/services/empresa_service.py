
from models.empresa import Empresa
from services.base import BaseService
from sqlalchemy.orm import Session

class EmpresaService(BaseService):
    def __init__(self, db: Session):
        super().__init__(Empresa)  # Passa a classe Empresa para a classe base
        self.db = db 





