from models.vetor import Vetor
from services.base import BaseService
from sqlalchemy.orm import Session
from pgvector.sqlalchemy import Vector

class VetorService(BaseService):
    def __init__(self, db: Session):
        super().__init__(Vetor)
        self.db = db 
