# backend/dependencies/empresa_dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.services.empresa_service import EmpresaService
from database.connection import get_db

def get_empresa_service(db: Session = Depends(get_db)) -> EmpresaService:
    return EmpresaService(db)
