from backend.models import Base
from sqlalchemy import Column, Integer, Text, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class TrechoSite(Base):
    __tablename__ = 'trechos_site'

    id = Column('id_trecho', Integer, primary_key=True)
    url = Column(Text, nullable=False)
    titulo_secao = Column(String(255), nullable=True)
    conteudo = Column(Text, nullable=False)
    hash_conteudo = Column(String(64), unique=True, nullable=False)
    ativo = Column(Boolean, default=True)
    criado_em = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    atualizado_em = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
