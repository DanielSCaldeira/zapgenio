from fastapi import APIRouter, Depends, HTTPException
from backend.dependencies.empresa_dependencies import get_empresa_service
from backend.services.empresa_service import EmpresaService
from backend.dto.empresa_dto import EmpresaCreate, EmpresaOut

router = APIRouter()

# Rota para listar todas as empresas (GET)
@router.get("/", response_model=list[EmpresaOut])
async def list_empresas(service: EmpresaService = Depends(get_empresa_service)):
    empresas = await service.list()
    return empresas

# Rota para obter uma empresa específica (GET)
@router.get("/{id}", response_model=EmpresaOut)
async def get_empresa(id: int, service: EmpresaService = Depends(get_empresa_service)):
    empresa = await service.get(id)
    if empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

# Rota para criar uma nova empresa (POST)
@router.post("/", response_model=EmpresaOut)
async def create_empresa(empresa: EmpresaCreate, service: EmpresaService = Depends(get_empresa_service)):
    return await service.create(empresa)

# Rota para atualizar uma empresa (PUT)
@router.put("/{id}", response_model=EmpresaOut)
async def update_empresa(id: int, empresa_in: dict, service: EmpresaService = Depends(get_empresa_service)):
    updated_empresa = await service.update(id, empresa_in)
    if updated_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return updated_empresa

# Rota para excluir uma empresa (DELETE)
@router.delete("/{id}", response_model=EmpresaOut)
async def delete_empresa(id: int, service: EmpresaService = Depends(get_empresa_service)):
    deleted_empresa = await service.delete(id)
    if deleted_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return deleted_empresa
