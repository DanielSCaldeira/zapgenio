from typing import List
from backend.models import Base, trecho_pergunta_resposta
from sqlalchemy import Column, Integer, Text,  TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.models.trecho_site import TrechoSite

class PerguntaResposta(Base):
    __tablename__ = 'perguntas_respostas'

    id = Column('id_pergunta_resposta', Integer, primary_key=True)
    id_lista_pergunta_resposta = Column(Integer, ForeignKey('listas_perguntas_respostas.id_lista_pergunta_resposta', ondelete='CASCADE'), nullable=False)
    pergunta = Column(Text, nullable=False)
    resposta = Column(Text, nullable=False)
    data_cadastro = Column(TIMESTAMP, server_default=func.now())

    vetores = relationship('Vetor')
    trechos: Mapped[List[TrechoSite]] = relationship(secondary=trecho_pergunta_resposta.trecho_pergunta_resposta)