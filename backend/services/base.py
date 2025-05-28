from typing import Type, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload, RelationshipProperty, class_mapper

class BaseService:
    def __init__(self, model, db: AsyncSession):
        self.model = model
        self.db = db

    def _get_all_relationship_options(self) -> List:
        """
        Retorna lista de opções selectinload para todos os relacionamentos do modelo.
        """
        mapper = class_mapper(self.model)
        options = []
        for prop in mapper.relationships:
            options.append(selectinload(getattr(self.model, prop.key)))
        return options

    async def list(self, load_all_relations: bool = False):
        stmt = select(self.model)
        if load_all_relations:
            options = self._get_all_relationship_options()
            stmt = stmt.options(*options)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def create(self, obj_in: dict):
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj

    async def get(self, id: int):
        result = await self.db.execute(select(self.model).filter(self.model.id == id))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100):
        result = await self.db.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def update(self, id: int, obj_in: dict):
        obj = await self.get(id)
        if not obj:
            return None
        for key, value in obj_in.items():
            setattr(obj, key, value)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj

    async def delete(self, id: int):
        obj = await self.get(id)
        if not obj:
            return None
        await self.db.delete(obj)
        await self.db.commit()
        return obj

