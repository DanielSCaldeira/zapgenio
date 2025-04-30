from pydantic import BaseModel
from backend.dto.usuario_dto import UsuarioBase

class EmpresaBase(BaseModel):
    id: int
    nome: str
    cnpj: str
    usuarios: list[UsuarioBase] = []

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(EmpresaBase):
    pass

class EmpresaOut(EmpresaBase):
    id: int

    class Config:
        from_attributes = True
