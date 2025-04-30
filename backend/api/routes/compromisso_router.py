from fastapi import APIRouter, Depends, HTTPException
from backend.dependencies.compromisso_dependencies import get_compromisso_service
from dto.compromisso_dto import CompromissoCreate, CompromissoOut
from services.compromisso_service import CompromissoService

router = APIRouter()

# Rota para listar todos os compromissos (GET)
@router.get("/", response_model=list[CompromissoOut])
def list_compromissos(service: CompromissoService = Depends(get_compromisso_service)):
    compromissos = service.list()
    return compromissos

# Rota para obter um compromisso específico (GET)
@router.get("/{id}", response_model=CompromissoOut)
def get_compromisso(id: int, service: CompromissoService = Depends(get_compromisso_service)):
    compromisso = service.get(id)
    if compromisso is None:
        raise HTTPException(status_code=404, detail="Compromisso não encontrado")
    return compromisso

# Rota para criar um novo compromisso (POST)
@router.post("/", response_model=CompromissoOut)
def create_compromisso(compromisso: CompromissoCreate, service: CompromissoService = Depends(get_compromisso_service)):
    return service.create(compromisso)

# Rota para atualizar um compromisso (PUT)
@router.put("/{id}", response_model=CompromissoOut)
def update_compromisso(id: int, compromisso_in: dict, service: CompromissoService = Depends(get_compromisso_service)):
    updated_compromisso = service.update(id, compromisso_in)
    if updated_compromisso is None:
        raise HTTPException(status_code=404, detail="Compromisso não encontrado")
    return updated_compromisso

# Rota para excluir um compromisso (DELETE)
@router.delete("/{id}", response_model=CompromissoOut)
def delete_compromisso(id: int, service: CompromissoService = Depends(get_compromisso_service)):
    deleted_compromisso = service.delete(id)
    if deleted_compromisso is None:
        raise HTTPException(status_code=404, detail="Compromisso não encontrado")
    return deleted_compromisso
