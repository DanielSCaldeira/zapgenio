from pydantic import BaseModel
from datetime import datetime

class CompromissoBase(BaseModel):
    titulo: str
    descricao: str
    data_inicio: datetime
    data_fim: datetime
    id_empresa: int
    arquivo_ics: str

class CompromissoCreate(CompromissoBase):
    pass

class CompromissoUpdate(CompromissoBase):
    pass

class CompromissoOut(CompromissoBase):
    id: int

    class Config:
        from_attributes = True
