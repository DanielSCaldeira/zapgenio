# backend/dependencies/compromisso_dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.services.compromisso_service import CompromissoService
from database.connection import get_db

def get_compromisso_service(db: Session = Depends(get_db)) -> CompromissoService:
    return CompromissoService(db)
