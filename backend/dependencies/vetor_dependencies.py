# backend/dependencies/vetor_dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.services.vetor_service import VetorService
from database.connection import get_db

def get_vetor_service(db: Session = Depends(get_db)) -> VetorService:
    return VetorService(db)
