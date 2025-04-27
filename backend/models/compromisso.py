from backend.models.empresa import Empresa
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Compromisso(Base):
    __tablename__ = 'compromissos'

    id = Column('id_compromisso',Integer, primary_key=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id_empresa', ondelete='CASCADE'), nullable=False)
    titulo = Column(String(255))
    descricao = Column(Text)
    data_inicio = Column(TIMESTAMP)
    data_fim = Column(TIMESTAMP)
    arquivo_ics = Column(Text)
    criado_em = Column(TIMESTAMP, server_default=func.now())

    empresa = relationship(Empresa)
