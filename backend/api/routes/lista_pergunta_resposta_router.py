from fastapi import APIRouter, Depends, HTTPException
from backend.dependencies.lista_pergunta_resposta_dependencies import get_lista_pergunta_resposta_service
from backend.dto.lista_pergunta_dto import ListaPerguntaRespostaCreate, ListaPerguntaRespostaOut
from backend.services.lista_pergunta_resposta_service import ListaPerguntaRespostaService

router =APIRouter()

# Rota para listar todas as listas de perguntas (GET)
@router.get("/", response_model=list[ListaPerguntaRespostaOut])
async def list_listas_perguntas(service: ListaPerguntaRespostaService = Depends(get_lista_pergunta_resposta_service)):
    listas_perguntas = await service.list()
    return listas_perguntas

# Rota para obter uma lista de perguntas específica (GET)
@router.get("/{id}", response_model=ListaPerguntaRespostaOut)
async def get_lista_pergunta(id: int, service: ListaPerguntaRespostaService = Depends(get_lista_pergunta_resposta_service)):
    lista_pergunta = await service.get(id)
    if lista_pergunta is None:
        raise HTTPException(status_code=404, detail="Lista de Perguntas não encontrada")
    return lista_pergunta

# Rota para criar uma nova lista de perguntas (POST)
@router.post("/", response_model=ListaPerguntaRespostaOut)
async def create_lista_pergunta(lista_pergunta: ListaPerguntaRespostaCreate, service: ListaPerguntaRespostaService = Depends(get_lista_pergunta_resposta_service)):
    return await service.create(lista_pergunta)

# Rota para atualizar uma lista de perguntas (PUT)
@router.put("/{id}", response_model=ListaPerguntaRespostaOut)
async def update_lista_pergunta(id: int, lista_pergunta_in: dict, service: ListaPerguntaRespostaService = Depends(get_lista_pergunta_resposta_service)):
    updated_lista_pergunta = await service.update(id, lista_pergunta_in)
    if updated_lista_pergunta is None:
        raise HTTPException(status_code=404, detail="Lista de Perguntas não encontrada")
    return updated_lista_pergunta

# Rota para excluir uma lista de perguntas (DELETE)
@router.delete("/{id}", response_model=ListaPerguntaRespostaOut)
async def delete_lista_pergunta(id: int, service: ListaPerguntaRespostaService = Depends(get_lista_pergunta_resposta_service)):
    deleted_lista_pergunta = await service.delete(id)
    if deleted_lista_pergunta is None:
        raise HTTPException(status_code=404, detail="Lista de Perguntas não encontrada")
    return deleted_lista_pergunta
