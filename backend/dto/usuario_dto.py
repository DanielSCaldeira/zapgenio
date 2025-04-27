from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    email: str
    id_empresa: int

class UsuarioCreate(UsuarioBase):
    senha: str  # Campo usado apenas na criação

class UsuarioUpdate(UsuarioBase):
    pass  # Pode ser ajustado conforme a lógica de atualização

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
