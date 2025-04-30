import uvicorn
from fastapi import FastAPI
from backend.api.routes import compromisso_router, empresa_router, pergunta_resposta_router, usuario_router, vetor_router,lista_pergunta_resposta_router 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="ZapGenio API - Teste",
    description="API para testes e validações",
    version="1.0.0-test"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Registrando rotas
app.include_router(usuario_router.router, prefix="/usuarios", tags=["Usuarios"],  responses={404: {"description": "Not found"}})
app.include_router(compromisso_router.router, prefix="/compromissos", tags=["Compromissos"])
app.include_router(empresa_router.router, prefix="/empresas", tags=["Empresas"])
app.include_router(lista_pergunta_resposta_router.router, prefix="/listas-perguntas-respostas", tags=["Listas de Perguntas"])
app.include_router(pergunta_resposta_router.router, prefix="/perguntas-respostas", tags=["Perguntas e Respostas"])
app.include_router(vetor_router.router, prefix="/vetores", tags=["Vetores"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)