from pydantic import BaseModel

class PerguntaRespostaBase(BaseModel):
    pergunta: str
    resposta: str

class PerguntaRespostaCreate(PerguntaRespostaBase):
    pass

class PerguntaRespostaUpdate(PerguntaRespostaBase):
    pass

class PerguntaRespostaOut(PerguntaRespostaBase):
    id: int

    class Config:
        orm_mode = True
