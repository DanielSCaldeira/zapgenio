from models import Base
from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func


class Vetor(Base):
    __tablename__ = 'vetores'

    id = Column('id_vetor',Integer, primary_key=True)
    id_pergunta_resposta = Column(Integer, ForeignKey('perguntas_respostas.id_pergunta_resposta', ondelete='CASCADE'), nullable=False)
    vetor = Column(Vector(1536), nullable=False)  # [{id_pergunta, vetor}]
    data_geracao = Column(TIMESTAMP, server_default=func.now())
    ativo = Column(Boolean, default=False)
