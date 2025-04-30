# backend/dependencies/pergunta_resposta_dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.services.pergunta_resposta_service import PerguntaRespostaService
from database.connection import get_db

def get_pergunta_resposta_service(db: Session = Depends(get_db)) -> PerguntaRespostaService:
    return PerguntaRespostaService(db)
