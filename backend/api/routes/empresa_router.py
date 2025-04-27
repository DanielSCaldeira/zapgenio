from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from dto.empresa_dto import EmpresaCreate, EmpresaOut
from services.empresa_service import EmpresaService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rota para listar todas as empresas (GET)
@router.get("/", response_model=list[EmpresaOut])
def list_empresas(db: Session = Depends(get_db)):
    service = EmpresaService(db)
    empresas = service.list()  # Aqui você chama o método list da EmpresaService
    return empresas

# Rota para obter uma empresa específica (GET)
@router.get("/{id_empresa}", response_model=EmpresaOut)
def get_empresa(id_empresa: int, db: Session = Depends(get_db)):
    service = EmpresaService(db)
    empresa = service.get(id_empresa)
    if empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

# Rota para criar uma nova empresa (POST)
@router.post("/", response_model=EmpresaOut)
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    service = EmpresaService(db)
    return service.create(empresa)

# Rota para atualizar uma empresa (PUT)
@router.put("/{id_empresa}", response_model=EmpresaOut)
def update_empresa(id_empresa: int, empresa_in: dict, db: Session = Depends(get_db)):
    service = EmpresaService(db)
    updated_empresa = service.update(id_empresa, empresa_in)
    if updated_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return updated_empresa

# Rota para excluir uma empresa (DELETE)
@router.delete("/{id_empresa}", response_model=EmpresaOut)
def delete_empresa(id_empresa: int, db: Session = Depends(get_db)):
    service = EmpresaService(db)
    deleted_empresa = service.delete(id_empresa)
    if deleted_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return deleted_empresa
