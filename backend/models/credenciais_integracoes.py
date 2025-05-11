from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.models import Base

class CredenciaisIntegracoes(Base):
    __tablename__ = 'credenciais_integracoes'

    id = Column('id_credencial', Integer, primary_key=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id_empresa', ondelete='CASCADE'), nullable=False)
    tipo_integracao = Column(Integer, nullable=False)
    chave_api = Column(Text, nullable=False)
    dados_adicionais = Column(JSON, nullable=True)
    webhook_url = Column(Text, nullable=True)
    phone_number_id = Column(String(255), nullable=True)
    token_expiracao = Column(TIMESTAMP, nullable=True)
    estado_integracao = Column(String(50), nullable=True)
    ativo = Column(Boolean, default=True)
    tentativas_falha = Column(Integer, default=0)
    criado_em = Column(TIMESTAMP, server_default=func.now())
    atualizado_em = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    usuario_criador = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=True)

    # Relacionamento (opcional, se necessário para acesso a dados das empresas ou usuários)
    empresa = relationship('Empresa', backref='credenciais_integracoes')
    usuario = relationship('Usuario', backref='credenciais_integracoes')

