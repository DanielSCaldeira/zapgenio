from logging.config import fileConfig
import os

from sqlalchemy import engine_from_config, pool
from alembic import context

# Importa sua Base de dados (assíncrona)
from models import *
from database.connection import Base
# Alembic Config object (carregado do alembic.ini)
config = context.config

# Configura logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Alvo da metadata para autogenerate
target_metadata = Base.metadata

# Lê a URL do banco de dados síncrono
DATABASE_URL = os.getenv("ALEMBIC_DATABASE_URL", "postgresql://postgres:123@localhost:5432/zapgenio")
config.set_main_option("sqlalchemy.url", DATABASE_URL)


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
