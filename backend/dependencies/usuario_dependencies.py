# backend/dependencies/usuario_dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.services.usuario_service import UsuarioService
from database.connection import get_db

def get_usuario_service(db: Session = Depends(get_db)) -> UsuarioService:
    return UsuarioService(db)
