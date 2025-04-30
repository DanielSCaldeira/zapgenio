# backend/dependencies/lista_pergunta_resposta_dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.services.lista_pergunta_resposta_service import ListaPerguntaRespostaService
from database.connection import get_db

def get_lista_pergunta_resposta_service(db: Session = Depends(get_db)) -> ListaPerguntaRespostaService:
    return ListaPerguntaRespostaService(db)
