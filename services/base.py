from sqlalchemy.orm import Session

class BaseService:
    def __init__(self, model):
        self.model = model

    def create(self, db: Session, obj_in: dict):
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()

    def update(self, db: Session, id: int, obj_in: dict):
        db_obj = db.query(self.model).filter(self.model.id == id).first()
        if not db_obj:
            return None
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int):
        db_obj = db.query(self.model).filter(self.model.id == id).first()
        if not db_obj:
            return None
        db.delete(db_obj)
        db.commit()
        return db_obj
