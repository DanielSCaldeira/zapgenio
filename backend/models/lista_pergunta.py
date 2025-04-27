from sqlalchemy import Column, Integer, String, Text,  TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class ListaPergunta(Base):
    __tablename__ = 'listas_perguntas'

    id = Column('id_lista',Integer, primary_key=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id_empresa', ondelete='CASCADE'), nullable=False)
    nome_lista = Column(String(255))
    descricao = Column(Text)
    data_criacao = Column(TIMESTAMP, server_default=func.now())

    empresa = relationship('Empresa', back_populates='listas_perguntas')
    perguntas_respostas = relationship('PerguntaResposta', back_populates='lista', cascade='all, delete-orphan')
    vetores = relationship('Vetor', back_populates='lista', cascade='all, delete-orphan')

