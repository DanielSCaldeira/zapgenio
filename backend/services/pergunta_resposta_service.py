from models.pergunta_resposta import PerguntaResposta
from services.base import BaseService
from sqlalchemy.orm import Session

class PerguntaRespostaService(BaseService):
    def __init__(self, db: Session):
        super().__init__(PerguntaResposta)
        self.db = db 
    
   