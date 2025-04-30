from pydantic import BaseModel
from datetime import datetime

class CompromissoBase(BaseModel):
    titulo: str
    descricao: str
    data: datetime
    empresa_id: int

class CompromissoCreate(CompromissoBase):
    pass

class CompromissoUpdate(CompromissoBase):
    pass

class CompromissoOut(CompromissoBase):
    id: int

    class Config:
        from_attributes = True
