from pydantic import BaseModel

from backend.dto.pergunta_resposta_dto import PerguntaRespostaBase

class ListaPerguntaRespostaBase(BaseModel):
    nome_lista: str
    descricao: str
    id_empresa: int
    perguntas_respostas: list[PerguntaRespostaBase]  # Assuming perguntas_respostas is a list of dictionaries
    

class ListaPerguntaRespostaCreate(ListaPerguntaRespostaBase):
    pass

class ListaPerguntaRespostaUpdate(ListaPerguntaRespostaBase):
    pass

class ListaPerguntaRespostaOut(ListaPerguntaRespostaBase):
    id: int

    class Config:
        from_attributes = True
