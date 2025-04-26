from models.pergunta_resposta import PerguntaResposta
from services.base import BaseService
from sqlalchemy.orm import Session

class PerguntaRespostaService(BaseService):
    def __init__(self):
        super().__init__(PerguntaResposta)

    def get(self, db: Session, id_pergunta: int):
        return db.query(self.model).filter(self.model.id_pergunta == id_pergunta).first()

    def update(self, db: Session, id_pergunta: int, obj_in: dict):
        db_obj = db.query(self.model).filter(self.model.id_pergunta == id_pergunta).first()
        if not db_obj:
            return None
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id_pergunta: int):
        db_obj = db.query(self.model).filter(self.model.id_pergunta == id_pergunta).first()
        if not db_obj:
            return None
        db.delete(db_obj)
        db.commit()
        return db_obj