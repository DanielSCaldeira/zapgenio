
from backend.models.lista_pergunta_resposta import ListaPerguntaResposta
from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession

class ListaPerguntaRespostaService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(ListaPerguntaResposta)
        self.db = db 
            

