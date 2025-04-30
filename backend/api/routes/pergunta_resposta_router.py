from fastapi import APIRouter, Depends, HTTPException
from backend.dependencies.pergunta_resposta_dependencies import get_pergunta_resposta_service
from dto.pergunta_resposta_dto import PerguntaRespostaCreate, PerguntaRespostaOut
from backend.services.pergunta_resposta_service import PerguntaRespostaService

router = APIRouter()

# Rota para listar todas as perguntas e respostas (GET)
@router.get("/", response_model=list[PerguntaRespostaOut])
def list_perguntas_respostas(service: PerguntaRespostaService = Depends(get_pergunta_resposta_service)):
    perguntas_respostas = service.list()
    return perguntas_respostas

# Rota para obter uma pergunta e resposta específica (GET)
@router.get("/{id}", response_model=PerguntaRespostaOut)
def get_pergunta_resposta(id: int, service: PerguntaRespostaService = Depends(get_pergunta_resposta_service)):
    pergunta_resposta = service.get(id)
    if pergunta_resposta is None:
        raise HTTPException(status_code=404, detail="Pergunta e Resposta não encontrada")
    return pergunta_resposta

# Rota para criar uma nova pergunta e resposta (POST)
@router.post("/", response_model=PerguntaRespostaOut)
def create_pergunta_resposta(pergunta_resposta: PerguntaRespostaCreate, service: PerguntaRespostaService = Depends(get_pergunta_resposta_service)):
    return service.create(pergunta_resposta)

# Rota para atualizar uma pergunta e resposta (PUT)
@router.put("/{id}", response_model=PerguntaRespostaOut)
def update_pergunta_resposta(id: int, pergunta_resposta_in: dict, service: PerguntaRespostaService = Depends(get_pergunta_resposta_service)):
    updated_pergunta_resposta = service.update(id, pergunta_resposta_in)
    if updated_pergunta_resposta is None:
        raise HTTPException(status_code=404, detail="Pergunta e Resposta não encontrada")
    return updated_pergunta_resposta

# Rota para excluir uma pergunta e resposta (DELETE)
@router.delete("/{id}", response_model=PerguntaRespostaOut)
def delete_pergunta_resposta(id: int, service: PerguntaRespostaService = Depends(get_pergunta_resposta_service)):
    deleted_pergunta_resposta = service.delete(id)
    if deleted_pergunta_resposta is None:
        raise HTTPException(status_code=404, detail="Pergunta e Resposta não encontrada")
    return deleted_pergunta_resposta
