"""Initial migration

Revision ID: 86a0790da1f0
Revises: 
Create Date: 2025-05-11 00:32:15.476276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '86a0790da1f0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('empresas')
    op.drop_table('compromissos')
    op.drop_index('idx_perguntas_respostas_id_lista_pergunta_resposta', table_name='perguntas_respostas')
    op.drop_table('perguntas_respostas')
    op.drop_index('vetores_idx', table_name='vetores', postgresql_using='ivfflat')
    op.drop_table('vetores')
    op.drop_index('idx_listas_perguntas_respostas_id_empresa', table_name='listas_perguntas_respostas')
    op.drop_table('listas_perguntas_respostas')
    op.drop_table('usuarios')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id_usuario', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_empresa', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nome', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('senha_hash', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('tipo_usuario', sa.VARCHAR(length=20), server_default=sa.text("'comum'::character varying"), autoincrement=False, nullable=True),
    sa.Column('ativo', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=True),
    sa.Column('data_cadastro', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresas.id_empresa'], name='usuarios_id_empresa_fkey'),
    sa.PrimaryKeyConstraint('id_usuario', name='usuarios_pkey'),
    sa.UniqueConstraint('email', name='usuarios_email_key')
    )
    op.create_table('listas_perguntas_respostas',
    sa.Column('id_lista_pergunta_resposta', sa.INTEGER(), server_default=sa.text("nextval('listas_perguntas_respostas_id_lista_pergunta_resposta_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('id_empresa', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nome_lista', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('descricao', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('data_criacao', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresas.id_empresa'], name='listas_perguntas_respostas_id_empresa_fkey'),
    sa.PrimaryKeyConstraint('id_lista_pergunta_resposta', name='listas_perguntas_respostas_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('idx_listas_perguntas_respostas_id_empresa', 'listas_perguntas_respostas', ['id_empresa'], unique=False)
    op.create_table('vetores',
    sa.Column('id_vetor', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_pergunta_resposta', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('vetor', sa.NullType(), autoincrement=False, nullable=False),
    sa.Column('data_geracao', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('data_atualizacao', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('ativo', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_pergunta_resposta'], ['perguntas_respostas.id_pergunta_resposta'], name='vetores_id_pergunta_resposta_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_vetor', name='vetores_pkey')
    )
    op.create_index('vetores_idx', 'vetores', ['vetor'], unique=False, postgresql_using='ivfflat')
    op.create_table('perguntas_respostas',
    sa.Column('id_pergunta_resposta', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_lista_pergunta_resposta', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pergunta', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('resposta', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('data_cadastro', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('data_atualizacao', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('ativo', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_lista_pergunta_resposta'], ['listas_perguntas_respostas.id_lista_pergunta_resposta'], name='perguntas_respostas_id_lista_pergunta_resposta_fkey'),
    sa.PrimaryKeyConstraint('id_pergunta_resposta', name='perguntas_respostas_pkey')
    )
    op.create_index('idx_perguntas_respostas_id_lista_pergunta_resposta', 'perguntas_respostas', ['id_lista_pergunta_resposta'], unique=False)
    op.create_table('compromissos',
    sa.Column('id_compromisso', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_empresa', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('titulo', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('descricao', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('data_inicio', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('data_fim', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('arquivo_ics', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('criado_em', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresas.id_empresa'], name='compromissos_id_empresa_fkey'),
    sa.PrimaryKeyConstraint('id_compromisso', name='compromissos_pkey')
    )
    op.create_table('empresas',
    sa.Column('id_empresa', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('cnpj', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('email_contato', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('telefone', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('data_cadastro', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_empresa', name='empresas_pkey')
    )
    # ### end Alembic commands ###
