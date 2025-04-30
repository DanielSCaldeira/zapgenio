from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

DBAsyncSession = async_sessionmaker()
Base = declarative_base()

async def initialize_sql(engine):
    DBAsyncSession.configure(bind=engine, class_=AsyncSession, expire_on_commit=False)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    
    
    
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import scoped_session, sessionmaker

# DBSession = scoped_session(sessionmaker())
# Base = declarative_base()

# def initialize_sql(engine):
#     DBSession.configure(bind=engine)
#     Base.metadata.bind = engine
#     Base.metadata.create_all(engine)