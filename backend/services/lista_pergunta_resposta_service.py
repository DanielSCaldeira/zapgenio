
from models.lista_pergunta_resposta import ListaPerguntaResposta
from services.base import BaseService
from sqlalchemy.orm import Session

class ListaPerguntaRespostaService(BaseService):
    def __init__(self, db: Session):
        super().__init__(ListaPerguntaResposta)
        self.db = db 
            

