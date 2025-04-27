from pydantic import BaseModel

class ListaPerguntaBase(BaseModel):
    titulo: str
    empresa_id: int
    perguntas_respostas: list[dict]  # Assuming perguntas_respostas is a list of dictionaries
    

class ListaPerguntaCreate(ListaPerguntaBase):
    pass

class ListaPerguntaUpdate(ListaPerguntaBase):
    pass

class ListaPerguntaOut(ListaPerguntaBase):
    id: int

    class Config:
        orm_mode = True
