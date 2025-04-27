
from models.lista_pergunta import ListaPergunta
from services.base import BaseService
from sqlalchemy.orm import Session

class ListaPerguntaService(BaseService):
    def __init__(self, db: Session):
        super().__init__(ListaPergunta)
        self.db = db 
            

