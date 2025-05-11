from fastapi import APIRouter, Depends, HTTPException
from backend.dependencies.credenciais_integracoes_dependencies import get_credenciais_integracoes_service
from backend.dto.credencias_integracoes_dto import CredenciaisIntegracoesCreate, CredenciaisIntegracoesOut
from backend.services.credencias_integracoes_service import CredenciaisIntegracoesService

router = APIRouter()

# Rota para listar todas as credenciais de integração (GET)
@router.get("/", response_model=list[CredenciaisIntegracoesOut])
async def list_credenciais_integracoes(service: CredenciaisIntegracoesService = Depends(get_credenciais_integracoes_service)):
    credenciais = await service.list()
    return credenciais

# Rota para obter uma credencial de integração específica (GET)
@router.get("/{id_credencial}", response_model=CredenciaisIntegracoesOut)
async def get_credencial(id_credencial: int, service: CredenciaisIntegracoesService = Depends(get_credenciais_integracoes_service)):
    credencial = await service.get(id_credencial)
    if credencial is None:
        raise HTTPException(status_code=404, detail="Credencial de integração não encontrada")
    return credencial

# Rota para criar uma nova credencial de integração (POST)
@router.post("/", response_model=CredenciaisIntegracoesOut)
async def create_credencial(credencial: CredenciaisIntegracoesCreate, service: CredenciaisIntegracoesService = Depends(get_credenciais_integracoes_service)):
    return await service.create(credencial)

# Rota para atualizar uma credencial de integração existente (PUT)
@router.put("/{id_credencial}", response_model=CredenciaisIntegracoesOut)
async def update_credencial(id_credencial: int, credencial_in: CredenciaisIntegracoesCreate, service: CredenciaisIntegracoesService = Depends(get_credenciais_integracoes_service)):
    updated_credencial = await service.update(id_credencial, credencial_in)
    if updated_credencial is None:
        raise HTTPException(status_code=404, detail="Credencial de integração não encontrada")
    return updated_credencial

# Rota para excluir uma credencial de integração (DELETE)
@router.delete("/{id_credencial}", response_model=CredenciaisIntegracoesOut)
async def delete_credencial(id_credencial: int, service: CredenciaisIntegracoesService = Depends(get_credenciais_integracoes_service)):
    deleted_credencial = await service.delete(id_credencial)
    if deleted_credencial is None:
        raise HTTPException(status_code=404, detail="Credencial de integração não encontrada")
    return deleted_credencial
