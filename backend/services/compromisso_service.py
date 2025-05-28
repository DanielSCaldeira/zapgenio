from backend.models.compromisso import Compromisso
from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession
from ics import Calendar, Event
from datetime import datetime

class CompromissoService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(Compromisso, db)
        self.db = db

    def gerar_ics(self, titulo: str, descricao: str, inicio: datetime, fim: datetime) -> str:
        c = Calendar()
        e = Event()
        e.name = titulo
        e.description = descricao
        e.begin = inicio
        e.end = fim
        c.events.add(e)
        return str(c)

    async def novo_compromisso(self, id_empresa: int, titulo: str, descricao: str, inicio: datetime, fim: datetime) -> Compromisso:
        
        arquivo_ics = self.gerar_ics(titulo, descricao, inicio, fim)
        novo = Compromisso(
            id_empresa=id_empresa,
            titulo=titulo,
            descricao=descricao,
            data_inicio=inicio,
            data_fim=fim,
            arquivo_ics=arquivo_ics
        )

        await self.create(novo)
        return novo

    async def buscarCompromisso(self, id: int) -> Compromisso:
        compromisso = await self.get(id)
        if compromisso and not compromisso.baixado:
            compromisso.baixado = True
            await self.update(id, compromisso)
        else:
            raise Exception("Compromisso não encontrado ou já baixado.")
        
        return compromisso.arquivo_ics

