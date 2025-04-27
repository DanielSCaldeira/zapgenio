from pydantic import BaseModel

from dto.pergunta_resposta_dto import PerguntaRespostaBase

class ListaPerguntaBase(BaseModel):
    nome_lista: str
    descricao: str
    id_empresa: int
    perguntas_respostas: list[PerguntaRespostaBase]  # Assuming perguntas_respostas is a list of dictionaries
    

class ListaPerguntaCreate(ListaPerguntaBase):
    pass

class ListaPerguntaUpdate(ListaPerguntaBase):
    pass

class ListaPerguntaOut(ListaPerguntaBase):
    id: int

    class Config:
        orm_mode = True
