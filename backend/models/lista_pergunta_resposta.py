from backend.models import Base
from sqlalchemy import Column, Integer, String, Text,  TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class ListaPerguntaResposta(Base):
    __tablename__ = 'listas_perguntas_respostas'

    id = Column('id_lista_pergunta_resposta',Integer, primary_key=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id_empresa', ondelete='CASCADE'), nullable=False)
    nome_lista = Column(String(255))
    descricao = Column(Text)
    data_criacao = Column(TIMESTAMP, server_default=func.now())

    # empresa = relationship('Empresa')
    perguntas_respostas = relationship('PerguntaResposta')

