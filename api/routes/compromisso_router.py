from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from dto.compromisso_dto import CompromissoCreate, CompromissoOut
from models.compromisso import Compromisso
from services.compromisso_service import CompromissoService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para listar todos os compromissos (GET)
@router.get("/", response_model=list[CompromissoOut])
def list_compromissos(db: Session = Depends(get_db)):
    service = CompromissoService(db)
    compromissos = service.list()
    return compromissos

# Rota para obter um compromisso específico (GET)
@router.get("/{id_compromisso}", response_model=CompromissoOut)
def get_compromisso(id_compromisso: int, db: Session = Depends(get_db)):
    service = CompromissoService(db)
    compromisso = service.get(id_compromisso)
    if compromisso is None:
        raise HTTPException(status_code=404, detail="Compromisso não encontrado")
    return compromisso

# Rota para criar um novo compromisso (POST)
@router.post("/", response_model=CompromissoOut)
def create_compromisso(compromisso: CompromissoCreate, db: Session = Depends(get_db)):
    service = CompromissoService(db)
    return service.create(compromisso)

# Rota para atualizar um compromisso (PUT)
@router.put("/{id_compromisso}", response_model=CompromissoOut)
def update_compromisso(id_compromisso: int, compromisso_in: dict, db: Session = Depends(get_db)):
    service = CompromissoService(db)
    updated_compromisso = service.update(id_compromisso, compromisso_in)
    if updated_compromisso is None:
        raise HTTPException(status_code=404, detail="Compromisso não encontrado")
    return updated_compromisso

# Rota para excluir um compromisso (DELETE)
@router.delete("/{id_compromisso}", response_model=CompromissoOut)
def delete_compromisso(id_compromisso: int, db: Session = Depends(get_db)):
    service = CompromissoService(db)
    deleted_compromisso = service.delete(id_compromisso)
    if deleted_compromisso is None:
        raise HTTPException(status_code=404, detail="Compromisso não encontrado")
    return deleted_compromisso
