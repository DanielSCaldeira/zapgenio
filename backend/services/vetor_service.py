from backend.models.vetor import Vetor
from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession
from pgvector.sqlalchemy import Vector
from openai import AsyncOpenAI
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models.pergunta_resposta import PerguntaResposta  # Importando os modelos
import os
from dotenv import load_dotenv
from sqlalchemy import select
import numpy as np
import re
import unicodedata

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("API_KEY_OPENAI"))

class VetorService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(Vetor, db)
        self.db = db 

    def salvar_vetor_npy(self, vetor, caminho_arquivo='vetor_embeddings.npy'):
        try:
            # Convertendo para NumPy array e salvando no formato .npy
            np.save(caminho_arquivo, np.array(vetor))
            print(f"Vetor salvo em {caminho_arquivo}")
        except Exception as e:
            print(f"Erro ao salvar vetor: {e}")
            
    def carregar_vetor_npy(self, caminho_arquivo='vetor_embeddings.npy'):
        try:
            # Carregando o vetor do arquivo .npy
            vetor = np.load(caminho_arquivo).tolist()
            print(f"Vetor carregado de {caminho_arquivo}")
            return vetor
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado")
            return None
        except Exception as e:
            print(f"Erro ao carregar vetor: {e}")
            return None
        
    def limpar_texto(self, texto: str) -> str:
        texto = texto.lower()
        texto = unicodedata.normalize('NFD', texto)
        texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')  # remove acentos
        texto = re.sub(r'[^\w\s]', '', texto)  # remove pontuação
        texto = re.sub(r'\s+', ' ', texto).strip()  # remove espaços extras
        return texto    
    
    async def gerar_embedding_pergunta(self, pergunta: str) -> list[float]:
        
        texto_formatado = self.limpar_texto(f"Pergunta: {pergunta}")
        
        response = await client.embeddings.create(
            model="text-embedding-ada-002",
            input= texto_formatado
        )
        vetor = response.data[0].embedding

        # Sanitize: garantir que é uma lista de floats 1D
        if not vetor or not isinstance(vetor, (list, tuple)):
            raise ValueError("Embedding retornado inválido")

        return vetor  

    async def buscar_similares(self, pergunta: str, top_k: int = 2):
        carregar_vetor_npy = self.carregar_vetor_npy()
        if carregar_vetor_npy is not None and len(carregar_vetor_npy) > 0:
            print(f"Vetor de embeddings carregado!")
            vetor_input = carregar_vetor_npy
        else:
            vetor_input = await self.gerar_embedding_pergunta(pergunta)
            self.salvar_vetor_npy(vetor_input)
            print("Nenhum vetor de embeddings encontrado.")
            
        print("Tipo do vetor:", type(vetor_input))
        print("Vetores (primeiros 5):", vetor_input[:5])

        # CTE para calcular a distância uma vez
        cte = (
            select(
                Vetor.id,
                Vetor.id_pergunta_resposta,
                Vetor.vetor.cosine_distance(vetor_input).label("distancia")
            )
            .cte("vetores_distancia")  # CTE nomeada
        )

        stmt = (
            select(
                cte.c.id,
                cte.c.id_pergunta_resposta,
                (1.0 - cte.c.distancia).label("similaridade")  # Converte a distância em similaridade
            )
            .where(cte.c.distancia <= 0.15)  # Filtro para similaridade >= 95%
            .order_by(cte.c.distancia)  # Ordena pela distância (menor distância = maior similaridade)
            .limit(top_k)
        )

        result = await self.db.execute(stmt)
        listResultado = result.fetchall()
        
        for idx, item in enumerate(listResultado, start=1):
            pergunta_resposta: PerguntaResposta = await self.db.get(PerguntaResposta, item.id_pergunta_resposta)
            print(f"Resultado {idx}: {pergunta_resposta.pergunta} -> {pergunta_resposta.resposta} -> similaridade: {item.similaridade}")
        
        return listResultado

    async def vetorizar_pergunta(self, pergunta_resposta: PerguntaResposta):
        try:
            prompt = f"{pergunta_resposta.pergunta}"
            response = await client.embeddings.create(
                model="text-embedding-3-small",
                input=prompt
            )
            vetor = response.data[0].embedding
            return vetor
        except Exception as e:
            print(f"Erro ao gerar vetor: {e}")
            return None

    async def salvar_vetor_na_base(self, pergunta_resposta_id: int, vetor: Vector) -> None:
        try:
            vetor_obj = Vetor(
                id_pergunta_resposta=pergunta_resposta_id,
                vetor=vetor,
                ativo=True
            )
            
            self.db.add(vetor_obj)
            await self.db.commit()
            await self.db.refresh(vetor_obj)
            print("Vetor salvo com sucesso!")
        except Exception as e:
            await self.db.rollback()
            print(f"Erro ao salvar vetor no banco de dados: {e}")
