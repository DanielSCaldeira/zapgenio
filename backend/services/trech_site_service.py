from backend.models.trecho_site import TrechoSite
from backend.services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession

class TrechoSiteService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(TrechoSite, db)
        self.db = db

