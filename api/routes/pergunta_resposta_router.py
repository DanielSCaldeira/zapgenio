from fastapi import APIRouter, Depends, HTTPException


from sqlalchemy.orm import Session
from database.connection import SessionLocal
from dto.pergunta_resposta_dto import PerguntaRespostaCreate, PerguntaRespostaOut
from services.pergunta_resposta_service import PerguntaRespostaService


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para listar todas as perguntas e respostas (GET)
@router.get("/", response_model=list[PerguntaRespostaOut])
def list_perguntas_respostas(db: Session = Depends(get_db)):
    service = PerguntaRespostaService(db)
    perguntas_respostas = service.list()
    return perguntas_respostas

# Rota para obter uma pergunta e resposta específica (GET)
@router.get("/{id_pergunta_resposta}", response_model=PerguntaRespostaOut)
def get_pergunta_resposta(id_pergunta_resposta: int, db: Session = Depends(get_db)):
    service = PerguntaRespostaService(db)
    pergunta_resposta = service.get(id_pergunta_resposta)
    if pergunta_resposta is None:
        raise HTTPException(status_code=404, detail="Pergunta e Resposta não encontrada")
    return pergunta_resposta

# Rota para criar uma nova pergunta e resposta (POST)
@router.post("/", response_model=PerguntaRespostaOut)
def create_pergunta_resposta(pergunta_resposta: PerguntaRespostaCreate, db: Session = Depends(get_db)):
    service = PerguntaRespostaService(db)
    return service.create(pergunta_resposta)

# Rota para atualizar uma pergunta e resposta (PUT)
@router.put("/{id_pergunta_resposta}", response_model=PerguntaRespostaOut)
def update_pergunta_resposta(id_pergunta_resposta: int, pergunta_resposta_in: dict, db: Session = Depends(get_db)):
    service = PerguntaRespostaService(db)
    updated_pergunta_resposta = service.update(id_pergunta_resposta, pergunta_resposta_in)
    if updated_pergunta_resposta is None:
        raise HTTPException(status_code=404, detail="Pergunta e Resposta não encontrada")
    return updated_pergunta_resposta

# Rota para excluir uma pergunta e resposta (DELETE)
@router.delete("/{id_pergunta_resposta}", response_model=PerguntaRespostaOut)
def delete_pergunta_resposta(id_pergunta_resposta: int, db: Session = Depends(get_db)):
    service = PerguntaRespostaService(db)
    deleted_pergunta_resposta = service.delete(id_pergunta_resposta)
    if deleted_pergunta_resposta is None:
        raise HTTPException(status_code=404, detail="Pergunta e Resposta não encontrada")
    return deleted_pergunta_resposta
