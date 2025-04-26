from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id_empresa', ondelete='CASCADE'), nullable=False)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha_hash = Column(Text, nullable=False)
    tipo_usuario = Column(String(20), default='comum')
    ativo = Column(Boolean, default=True)
    data_cadastro = Column(TIMESTAMP, server_default=func.now())

    empresa = relationship('Empresa', back_populates='usuarios')
