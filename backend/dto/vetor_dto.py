from pydantic import BaseModel
from typing import List

class VetorBase(BaseModel):
    pergunta_resposta_id: int
    vetor: List[float]

class VetorCreate(VetorBase):
    pass

class VetorUpdate(VetorBase):
    pass

class VetorOut(VetorBase):
    id: int

    class Config:
        orm_mode = True
