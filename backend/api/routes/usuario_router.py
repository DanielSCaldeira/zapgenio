from fastapi import APIRouter, Depends,  HTTPException
from backend.dependencies.usuario_dependencies import get_usuario_service
from backend.dto.usuario_dto import UsuarioCreate, UsuarioOut
from backend.services.usuario_service import UsuarioService

router = APIRouter()

@router.post("/", response_model=UsuarioOut)
async def create_usuario(usuario: UsuarioCreate,service: UsuarioService = Depends(get_usuario_service)):
    novo_usuario = await service.create(usuario)
    return novo_usuario

@router.get("/", response_model=list[UsuarioOut])
async def list_usuarios(service: UsuarioService = Depends(get_usuario_service)):
    usuarios = await service.list()
    return usuarios

@router.get("/{id}", response_model=UsuarioOut)
async def get_usuario(id: int, service: UsuarioService = Depends(get_usuario_service)):
    usuario = await service.get(id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.put("/{id}", response_model=UsuarioOut)
async def update_usuario(id: int, usuario: UsuarioCreate, service: UsuarioService = Depends(get_usuario_service)):
    updated_usuario = await service.update(id, usuario)
    if updated_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return updated_usuario

@router.delete("/{id}", response_model=UsuarioOut)
async def delete_usuario(id: int, service: UsuarioService = Depends(get_usuario_service)):
    deleted_usuario = await service.delete(id)
    if deleted_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return deleted_usuario
