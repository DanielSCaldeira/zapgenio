from models.vetor import Vetor
from services.base import BaseService
from sqlalchemy.orm import Session

class VetorService(BaseService):
    def __init__(self):
        super().__init__(Vetor)

    def get(self, db: Session, id_vetor: int):
        return db.query(self.model).filter(self.model.id_vetor == id_vetor).first()

    def update(self, db: Session, id_vetor: int, obj_in: dict):
        db_obj = db.query(self.model).filter(self.model.id_vetor == id_vetor).first()
        if not db_obj:
            return None
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id_vetor: int):
        db_obj = db.query(self.model).filter(self.model.id_vetor == id_vetor).first()
        if not db_obj:
            return None
        db.delete(db_obj)
        db.commit()
        return db_obj