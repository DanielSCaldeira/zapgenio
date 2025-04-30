from backend.models.vetor import Vetor
from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession
from pgvector.sqlalchemy import Vector
from openai import OpenAI
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models.pergunta_resposta import PerguntaResposta  # Importando os modelos
import os
from dotenv import load_dotenv
load_dotenv()


class VetorService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(Vetor, db)
        self.db = db 

    def vetorizar_pergunta_resposta(self, pergunta_resposta: PerguntaResposta):
            client = OpenAI(api_key=os.getenv("API_KEY_OPENAI"))
            
            try:
                prompt = f"Pergunta: {pergunta_resposta.pergunta}\nResposta: {pergunta_resposta.resposta}"
                
                response = client.embeddings.create(
                    model="text-embedding-3-small",
                    input=prompt
                )
                
                vetor = response.data[0].embedding
                return vetor
            except Exception as e:
                print(f"Erro ao gerar vetor: {e}")
                return None

    async def salvar_vetor_na_base(self, pergunta_resposta_id: int, vetor: Vector):
        try:
            vetor_obj = Vetor(
                id_pergunta_resposta=pergunta_resposta_id,
                vetor=vetor,
                ativo=True
            )
            
            # Adiciona e comita no banco de dados
            self.db.add(vetor_obj)
            await self.db.commit()
            print("Vetor salvo com sucesso!")
        except Exception as e:
            self.db.rollback()
            print(f"Erro ao salvar vetor no banco de dados: {e}")

    # Função principal que recebe a pergunta_resposta e realiza as operações
    def processar_pergunta_resposta(self, pergunta_resposta: PerguntaResposta):
        # Vetoriza a pergunta e resposta
        vetor =  self.vetorizar_pergunta_resposta(pergunta_resposta)
        
        if vetor:
            # Salva o vetor na base de dados
            self.salvar_vetor_na_base(pergunta_resposta.id, vetor)
