from services.base import BaseService
from sqlalchemy.orm import Session
from models.usuario import Usuario

class UsuarioService(BaseService):  # Corrigido: Use 'class' para definir uma classe
    def __init__(self):
        super().__init__(Usuario)

    def get(self, db: Session, id_usuario: int):
        return db.query(self.model).filter(self.model.id_usuario == id_usuario).first()

    def update(self, db: Session, id_usuario: int, obj_in: dict):
        db_obj = db.query(self.model).filter(self.model.id_usuario == id_usuario).first()
        if not db_obj:
            return None
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id_usuario: int):
        db_obj = db.query(self.model).filter(self.model.id_usuario == id_usuario).first()
        if not db_obj:
            return None
        db.delete(db_obj)
        db.commit()
        return db_obj

