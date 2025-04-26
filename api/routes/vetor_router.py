from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from dto.vetor_dto import VetorCreate, VetorOut
from models.vetor import Vetor
from services.vetor import VetorService

router =APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para listar todos os vetores (GET)
@router.get("/", response_model=list[VetorOut])
def list_vetores(db: Session = Depends(get_db)):
    service = VetorService(db)
    vetores = service.list()
    return vetores

# Rota para obter um vetor específico (GET)
@router.get("/{id_vetor}", response_model=VetorOut)
def get_vetor(id_vetor: int, db: Session = Depends(get_db)):
    service = VetorService(db)
    vetor = service.get(id_vetor)
    if vetor is None:
        raise HTTPException(status_code=404, detail="Vetor não encontrado")
    return vetor

# Rota para criar um novo vetor (POST)
@router.post("/", response_model=VetorOut)
def create_vetor(vetor: VetorCreate, db: Session = Depends(get_db)):
    service = VetorService(db)
    return service.create(vetor)

# Rota para atualizar um vetor (PUT)
@router.put("/{id_vetor}", response_model=VetorOut)
def update_vetor(id_vetor: int, vetor_in: dict, db: Session = Depends(get_db)):
    service = VetorService(db)
    updated_vetor = service.update(id_vetor, vetor_in)
    if updated_vetor is None:
        raise HTTPException(status_code=404, detail="Vetor não encontrado")
    return updated_vetor

# Rota para excluir um vetor (DELETE)
@router.delete("/{id_vetor}", response_model=VetorOut)
def delete_vetor(id_vetor: int, db: Session = Depends(get_db)):
    service = VetorService(db)
    deleted_vetor = service.delete(id_vetor)
    if deleted_vetor is None:
        raise HTTPException(status_code=404, detail="Vetor não encontrado")
    return deleted_vetor
