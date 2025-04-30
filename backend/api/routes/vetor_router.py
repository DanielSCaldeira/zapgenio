from fastapi import APIRouter, Depends, HTTPException
from backend.dependencies.vetor_dependencies import get_vetor_service
from dto.vetor_dto import VetorCreate, VetorOut
from backend.services.vetor_service import VetorService

router = APIRouter()

# Rota para listar todos os vetores (GET)
@router.get("/", response_model=list[VetorOut])
def list_vetores(service: VetorService = Depends(get_vetor_service)):
    vetores = service.list()
    return vetores

# Rota para obter um vetor específico (GET)
@router.get("/{id}", response_model=VetorOut)
def get_vetor(id: int, service: VetorService = Depends(get_vetor_service)):
    vetor = service.get(id)
    if vetor is None:
        raise HTTPException(status_code=404, detail="Vetor não encontrado")
    return vetor

# Rota para criar um novo vetor (POST)
@router.post("/", response_model=VetorOut)
def create_vetor(vetor: VetorCreate, service: VetorService = Depends(get_vetor_service)):
    return service.create(vetor)

# Rota para atualizar um vetor (PUT)
@router.put("/{id}", response_model=VetorOut)
def update_vetor(id: int, vetor_in: dict, service: VetorService = Depends(get_vetor_service)):
    updated_vetor = service.update(id, vetor_in)
    if updated_vetor is None:
        raise HTTPException(status_code=404, detail="Vetor não encontrado")
    return updated_vetor

# Rota para excluir um vetor (DELETE)
@router.delete("/{id}", response_model=VetorOut)
def delete_vetor(id: int, service: VetorService = Depends(get_vetor_service)):
    deleted_vetor = service.delete(id)
    if deleted_vetor is None:
        raise HTTPException(status_code=404, detail="Vetor não encontrado")
    return deleted_vetor
