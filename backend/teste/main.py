import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from backend.models import initialize_sql  # Ajuste aqui
from backend.database.connection import SessionLocal
from backend.models.pergunta_resposta import PerguntaResposta
from backend.services.vetor_service import VetorService

def main():
    with SessionLocal() as db:
        id = 1  # Substitua pelo ID real que deseja buscar
        pergunta_resposta = db.get(PerguntaResposta, id)
        if pergunta_resposta:
            vetorService = VetorService(db)
            vetorService.processar_pergunta_resposta(pergunta_resposta)
        else:
            print(f"PerguntaResposta com ID {id} não encontrada.")

if __name__ == "__main__":
    main()
        