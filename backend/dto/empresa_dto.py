from pydantic import BaseModel

from dto.usuario_dto import UsuarioBase

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
