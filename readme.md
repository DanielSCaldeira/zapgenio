# Zap Genio

## Resumo da Aplicação

Za Genio é um sistema web completo que integra um backend em Python (API REST), frontend em ReactJS com TailwindCSS e a inteligência da OpenAI para automatizar respostas via WhatsApp. A plataforma permite que clientes (empresas) cadastrem listas de perguntas e respostas, agendem compromissos e consultem históricos de vetores com controle de versões, tudo isso com um sistema de gestão de usuários e permissões por empresa.

## Módulos Principais

1.  **Empresas e Usuários:**
    * Controle de login, permissões e gestão de dados por empresa.
    * Permite que cada empresa (cliente) tenha múltiplos usuários.

2.  **Listas de Perguntas e Respostas:**
    * Cada lista possui um ID único e é vinculada a uma empresa.
    * As perguntas e respostas são organizadas por lista.
    * Suporte a múltiplas listas por empresa.

3.  **Vetorização:**
    * Histórico de vetores gerados ao longo do tempo para cada lista.
    * Indicação do vetor ativo para cálculo de similaridade.

4.  **Integração com WhatsApp:**
    * Comparação de mensagens recebidas com vetores ativos para respostas diretas.
    * Integração com ChatGPT para perguntas sem correspondência exata, utilizando um prompt personalizado.

5.  **Agenda e Compromissos:**
    * Criação de eventos por usuários.
    * Geração de arquivo `.ics` para cada compromisso.
    * Salvamento de dados na tabela de compromissos.
    * Link para adicionar o compromisso em agendas pessoais (Google Agenda, Outlook, etc.).

6.  **Interface Web:**
    * Tela única para visualização, adição, edição e exclusão de perguntas e respostas.
    * Botão para reprocessar vetores e armazenar novas versões.

## Modelagem de Dados (SQL)

```sql
-- Tabela de empresas
CREATE TABLE empresas (
    id_empresa SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cnpj VARCHAR(20),
    email_contato VARCHAR(255),
    telefone VARCHAR(20),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de usuários
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    id_empresa INT REFERENCES empresas(id_empresa),
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    tipo_usuario VARCHAR(20) DEFAULT 'comum',
    ativo BOOLEAN DEFAULT TRUE,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de listas de perguntas
CREATE TABLE listas_perguntas (
    id_lista SERIAL PRIMARY KEY,
    id_empresa INT REFERENCES empresas(id_empresa),
    nome_lista VARCHAR(255),
    descricao TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de perguntas e respostas
CREATE TABLE perguntas_respostas (
    id_pergunta SERIAL PRIMARY KEY,
    id_lista INT REFERENCES listas_perguntas(id_lista),
    pergunta TEXT NOT NULL,
    resposta TEXT NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de vetores
CREATE TABLE vetores (
    id_vetor SERIAL PRIMARY KEY,
    id_lista INT REFERENCES listas_perguntas(id_lista),
    vetor JSONB NOT NULL,
    data_geracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT FALSE
);

-- Tabela de compromissos
CREATE TABLE compromissos (
    id_compromisso SERIAL PRIMARY KEY,
    id_empresa INT REFERENCES empresas(id_empresa),
    titulo VARCHAR(255),
    descricao TEXT,
    data_inicio TIMESTAMP,
    data_fim TIMESTAMP,
    arquivo_ics TEXT,  -- base64 ou caminho do arquivo
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);