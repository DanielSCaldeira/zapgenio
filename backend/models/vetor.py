from sqlalchemy import Column, Integer, Boolean, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Vetor(Base):
    __tablename__ = 'vetores'

    id_vetor = Column(Integer, primary_key=True)
    id_lista = Column(Integer, ForeignKey('listas_perguntas.id_lista', ondelete='CASCADE'), nullable=False)
    vetor = Column(JSON, nullable=False)  # [{id_pergunta, vetor}]
    data_geracao = Column(TIMESTAMP, server_default=func.now())
    ativo = Column(Boolean, default=False)

    lista = relationship('ListaPergunta', back_populates='vetores')
