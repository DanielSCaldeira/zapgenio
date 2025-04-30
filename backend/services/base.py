from sqlalchemy.ext.asyncio import AsyncSession

class BaseService:
    def __init__(self, model):
        self.model = model

    async def list(self):
        return await self.db.query(self.model).all()

    async def create(self, db: AsyncSession, obj_in: dict):
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get(self, db: AsyncSession, id: int):
        return await db.query(self.model).filter(self.model.id == id).first()

    async def get_all(self, db: AsyncSession, skip: int = 0, limit: int = 100):
        return await db.query(self.model).offset(skip).limit(limit).all()

    async def update(self, db: AsyncSession, id: int, obj_in: dict):
        db_obj = await db.query(self.model).filter(self.model.id == id).first()
        if not db_obj:
            return None
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, id: int):
        db_obj = await db.query(self.model).filter(self.model.id == id).first()
        if not db_obj:
            return None
        await db.delete(db_obj)
        await db.commit()
        return db_obj
