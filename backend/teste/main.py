# main.py
from services.vetor import VetorService
from database.connection import SessionLocal
from models.pergunta_resposta import PerguntaResposta


def main():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    pergunta_resposata = db.get(PerguntaResposta, id)     
    vetorService = VetorService(db)    
    vetorService.processar_pergunta_resposta(pergunta_resposata)   


        