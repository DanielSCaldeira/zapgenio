from pydantic import BaseModel
from typing import List

class VetorBase(BaseModel):
    id_pergunta_resposta: int
    vetor: List[float]

class VetorCreate(VetorBase):
    pass

class VetorUpdate(VetorBase):
    pass

class VetorOut(VetorBase):
    id: int

    class Config:
        from_attributes = True
