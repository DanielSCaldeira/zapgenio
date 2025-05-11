# backend/models/trecho_pergunta_resposta.py
from sqlalchemy import Table, Column, ForeignKey, Integer
from backend.models import Base

trecho_pergunta_resposta = Table(
    'trecho_pergunta_resposta',
    Base.metadata,
    Column('id_pergunta_resposta',  ForeignKey('perguntas_respostas.id_pergunta_resposta', ondelete='CASCADE'), primary_key=True),
    Column('id_trecho_site', ForeignKey('trechos_site.id_trecho', ondelete='CASCADE'), primary_key=True),
)
