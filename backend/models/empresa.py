from backend.models import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func



class Empresa(Base):
    __tablename__ = 'empresas'

    id = Column('id_empresa',Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    cnpj = Column(String(20))
    email_contato = Column(String(255))
    telefone = Column(String(20))
    data_cadastro = Column(TIMESTAMP, server_default=func.now())
    compromissos = relationship('Compromisso')
