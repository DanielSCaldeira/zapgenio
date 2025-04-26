from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Empresa(Base):
    __tablename__ = 'empresas'

    id_empresa = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    cnpj = Column(String(20))
    email_contato = Column(String(255))
    telefone = Column(String(20))
    data_cadastro = Column(TIMESTAMP, server_default=func.now())

    usuarios = relationship('Usuario', back_populates='empresa', cascade='all, delete-orphan')
    listas_perguntas = relationship('ListaPergunta', back_populates='empresa', cascade='all, delete-orphan')
    compromissos = relationship('Compromisso', back_populates='empresa', cascade='all, delete-orphan')
