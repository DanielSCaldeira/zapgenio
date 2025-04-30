from backend.models.pergunta_resposta import PerguntaResposta
from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession

class PerguntaRespostaService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(PerguntaResposta)
        self.db = db 
    
   