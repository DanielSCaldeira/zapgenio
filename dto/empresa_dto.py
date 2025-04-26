from pydantic import BaseModel

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(EmpresaBase):
    pass

class EmpresaOut(EmpresaBase):
    id: int

    class Config:
        orm_mode = True
