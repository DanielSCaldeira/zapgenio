from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Esquema base para CredenciaisIntegracoes
class CredenciaisIntegracoesBase(BaseModel):
    id_empresa: int
    tipo_integracao: int
    chave_api: str
    dados_adicionais: Optional[dict] = None
    webhook_url: Optional[str] = None
    phone_number_id: Optional[str] = None
    token_expiracao: Optional[datetime] = None
    estado_integracao: Optional[str] = None
    ativo: Optional[bool] = True
    tentativas_falha: Optional[int] = 0
    usuario_criador: Optional[int] = None

# Esquema para criação de CredenciaisIntegracoes
class CredenciaisIntegracoesCreate(CredenciaisIntegracoesBase):
    pass

# Esquema para atualização de CredenciaisIntegracoes
class CredenciaisIntegracoesUpdate(CredenciaisIntegracoesBase):
    pass

# Esquema de saída de CredenciaisIntegracoes
class CredenciaisIntegracoesOut(CredenciaisIntegracoesBase):
    id_credencial: int
    criado_em: datetime
    atualizado_em: datetime

    class Config:
       from_attributes = True
