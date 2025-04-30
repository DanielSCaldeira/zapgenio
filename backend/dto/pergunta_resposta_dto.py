from pydantic import BaseModel

class PerguntaRespostaBase(BaseModel):
    id: int
    pergunta: str
    resposta: str

class PerguntaRespostaCreate(PerguntaRespostaBase):
    pass

class PerguntaRespostaUpdate(PerguntaRespostaBase):
    pass

class PerguntaRespostaOut(PerguntaRespostaBase):
    id: int

    class Config:
        from_attributes = True
