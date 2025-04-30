from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carrega o arquivo .env para acessar as variáveis de ambiente
load_dotenv()

def get_database_url():
    """
    Obtém a URL do banco de dados a partir das variáveis de ambiente.
    Caso a variável DATABASE_URL não seja encontrada, levanta um erro.
    """
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("A variável de ambiente DATABASE_URL não foi async definida.")
    return database_url

# Cria a engine de conexão com o banco de dados
engine = create_async_engine(get_database_url(), echo=True)

# Cria uma fábrica de sessões
AsyncAsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Classe base para os modelos (todas as classes que representam tabelas herdarão dessa)
Base = declarative_base()


async def get_db():
    """
Função auxiliar para fornecer uma sessão de banco de dados para as rotas do FastAPI.
Utiliza dependências para gerenciar o ciclo de vida da sessão.
"""
    async with AsyncAsyncSessionLocal() as AsyncSession:
        yield AsyncSession
