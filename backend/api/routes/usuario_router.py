from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from dto.usuario_dto import UsuarioCreate, UsuarioOut
from services.usuario_service import UsuarioService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UsuarioOut)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    novo_usuario = service.create(usuario)
    return novo_usuario

@router.get("/", response_model=list[UsuarioOut])
def list_usuarios(db: Session = Depends(get_db)):
    service = UsuarioService(db)
    usuarios = service.list()
    return usuarios

@router.get("/{id_usuario}", response_model=UsuarioOut)
def get_usuario(id_usuario: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    usuario = service.get(id_usuario)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.put("/{id_usuario}", response_model=UsuarioOut)
def update_usuario(id_usuario: int, usuario_in: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    updated_usuario = service.update(id_usuario, usuario_in)
    if updated_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return updated_usuario

@router.delete("/{id_usuario}", response_model=UsuarioOut)
def delete_usuario(id_usuario: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    deleted_usuario = service.delete(id_usuario)
    if deleted_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return deleted_usuario
