import sys
import os
import asyncio
from backend.services.pergunta_resposta_service import PerguntaRespostaService

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from backend.models import initialize_sql  # Ajuste aqui
from backend.database.connection import AsyncSessionLocal
from backend.models.pergunta_resposta import PerguntaResposta
from backend.services.vetor_service import VetorService


async def main():
    async with AsyncSessionLocal() as db:
        # id = 1  # Substitua pelo ID real que deseja buscar
        # lista: list[PerguntaResposta] = await PerguntaRespostaService(db).list()

        # for pergunta_resposta in lista:
        #     if pergunta_resposta:
        #         vetorService = VetorService(db)
        #         vetor = await vetorService.gerar_embedding_pergunta(pergunta_resposta.pergunta)
        #         await vetorService.salvar_vetor_na_base(pergunta_resposta.id, vetor)
        #     else:
        #         print(f"PerguntaResposta com ID {id} não encontrada.")
        vetorService = VetorService(db)
        g = await vetorService.buscar_similares("Qual é o horário de funcionamento?")
        print(g)

# Roda a função principal
if __name__ == "__main__":
    asyncio.run(main())

