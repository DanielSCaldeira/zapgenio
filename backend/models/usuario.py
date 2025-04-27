from models.empresa import Empresa
from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func

class Base(DeclarativeBase):
      pass

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column('id_usuario',Integer, primary_key=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id_empresa', ondelete='CASCADE'), nullable=False)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha_hash = Column(Text, nullable=False)
    tipo_usuario = Column(String(20), default='comum')
    ativo = Column(Boolean, default=True)
    data_cadastro = Column(TIMESTAMP, server_default=func.now())

    empresa = relationship(Empresa)
