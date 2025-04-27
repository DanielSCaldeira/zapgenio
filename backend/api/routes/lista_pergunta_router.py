from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from dto.lista_pergunta_dto import ListaPerguntaCreate, ListaPerguntaOut
from services.lista_pergunta_service import ListaPerguntaService

router =APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para listar todas as listas de perguntas (GET)
@router.get("/", response_model=list[ListaPerguntaOut])
def list_listas_perguntas(db: Session = Depends(get_db)):
    service = ListaPerguntaService(db)
    listas_perguntas = service.list()
    return listas_perguntas

# Rota para obter uma lista de perguntas específica (GET)
@router.get("/{id_lista_pergunta}", response_model=ListaPerguntaOut)
def get_lista_pergunta(id_lista_pergunta: int, db: Session = Depends(get_db)):
    service = ListaPerguntaService(db)
    lista_pergunta = service.get(id_lista_pergunta)
    if lista_pergunta is None:
        raise HTTPException(status_code=404, detail="Lista de Perguntas não encontrada")
    return lista_pergunta

# Rota para criar uma nova lista de perguntas (POST)
@router.post("/", response_model=ListaPerguntaOut)
def create_lista_pergunta(lista_pergunta: ListaPerguntaCreate, db: Session = Depends(get_db)):
    service = ListaPerguntaService(db)
    return service.create(lista_pergunta)

# Rota para atualizar uma lista de perguntas (PUT)
@router.put("/{id_lista_pergunta}", response_model=ListaPerguntaOut)
def update_lista_pergunta(id_lista_pergunta: int, lista_pergunta_in: dict, db: Session = Depends(get_db)):
    service = ListaPerguntaService(db)
    updated_lista_pergunta = service.update(id_lista_pergunta, lista_pergunta_in)
    if updated_lista_pergunta is None:
        raise HTTPException(status_code=404, detail="Lista de Perguntas não encontrada")
    return updated_lista_pergunta

# Rota para excluir uma lista de perguntas (DELETE)
@router.delete("/{id_lista_pergunta}", response_model=ListaPerguntaOut)
def delete_lista_pergunta(id_lista_pergunta: int, db: Session = Depends(get_db)):
    service = ListaPerguntaService(db)
    deleted_lista_pergunta = service.delete(id_lista_pergunta)
    if deleted_lista_pergunta is None:
        raise HTTPException(status_code=404, detail="Lista de Perguntas não encontrada")
    return deleted_lista_pergunta
