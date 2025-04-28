from models import Base
from sqlalchemy import Column, Integer, Text,  TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class PerguntaResposta(Base):
    __tablename__ = 'perguntas_respostas'

    id = Column('id_pergunta_resposta', Integer, primary_key=True)
    id_lista_pergunta_resposta = Column(Integer, ForeignKey('listas_perguntas_respostas.id_lista_pergunta_resposta', ondelete='CASCADE'), nullable=False)
    pergunta = Column(Text, nullable=False)
    resposta = Column(Text, nullable=False)
    data_cadastro = Column(TIMESTAMP, server_default=func.now())

    vetores = relationship('Vetor')
    
