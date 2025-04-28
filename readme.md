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
CREATE EXTENSION vector;

-- Tabela de empresas
CREATE TABLE empresas (
    id_empresa SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cnpj VARCHAR(20),
    email_contato VARCHAR(255),
    telefone VARCHAR(20),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



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


-- Tabela de listas de perguntas e respostas
CREATE TABLE listas_perguntas_respostas (
    id_lista_pergunta_resposta SERIAL PRIMARY KEY,
    id_empresa INT REFERENCES empresas(id_empresa),
    nome_lista VARCHAR(255),
    descricao TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de perguntas e respostas
CREATE TABLE perguntas_respostas (
    id_pergunta_resposta SERIAL PRIMARY KEY,
    id_lista_pergunta_resposta INT REFERENCES listas_perguntas_respostas(id_lista_pergunta_resposta), 
    pergunta TEXT NOT NULL,
    resposta TEXT NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT FALSE
);

-- Tabela de vetores
CREATE TABLE vetores (
    id_vetor SERIAL PRIMARY KEY,
    id_pergunta_resposta INT REFERENCES perguntas_respostas(id_pergunta_resposta) ON DELETE CASCADE,  
    vetor vector(1536) NOT NULL,  -- Usando o tipo "vector" da extensão instalada
    data_geracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT FALSE
);

-- Índices para otimizar consultas
CREATE INDEX idx_perguntas_respostas_id_lista_pergunta_resposta ON perguntas_respostas(id_lista_pergunta_resposta);
CREATE INDEX idx_listas_perguntas_respostas_id_empresa ON listas_perguntas_respostas(id_empresa);
CREATE INDEX vetores_idx ON vetores USING ivfflat (vetor);

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


# Zap Genio

## Resumo da Aplicação

Zap Genio é um sistema web completo que integra um backend em Python (API REST), frontend em ReactJS com TailwindCSS e a inteligência da OpenAI para automatizar respostas via WhatsApp.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados no seu ambiente:

- [Docker](https://www.docker.com/)
- [Node.js](https://nodejs.org/) (versão 16 ou superior)
- [npm](https://www.npmjs.com/) ou [yarn](https://yarnpkg.com/)
- [Python](https://www.python.org/) (versão 3.10 ou superior)
- [Poetry](https://python-poetry.org/) (opcional, para gerenciar dependências Python)
- [docker](https://docs.docker.com/desktop/setup/install/windows-install/)(docker)
- [pgvector-postgresql](https://github.com/pgvector/pgvector)(vector)

https://github.com/timescale/pgai

## Configuração do Backend

1. **Configurar variáveis de ambiente**:
   - Crie um arquivo `.env` na pasta `backend` com o seguinte conteúdo:
     ```env
     DATABASE_URL=postgresql://usuario:senha@localhost:5432/zapgenio
     ```

2. **Instalar dependências**:
   - Se estiver usando Docker, pule esta etapa.
   - Caso contrário, instale as dependências Python:
     ```bash
     cd backend
     pip install -r requirements.txt
     ```

3. **Executar migrações do banco de dados**:
   - Rode o comando:
     ```bash
     cd backend
     alembic upgrade head
     ```

4. **Iniciar o backend**:
   - Com Docker:
     ```bash
     cd backend
     docker-compose up
     ```
   - Sem Docker:
     ```bash
     cd backend
     uvicorn api.main:app --reload
     ```

## Configuração do Frontend

1. **Instalar dependências**:
   ```bash
   cd frontend
   npm install
   ```

2. **Iniciar o frontend**:
   ```bash
   npm run dev
   ```

3. **Acessar a aplicação**:
   - O frontend estará disponível em `http://localhost:5173`.

## Executar o Projeto Completo

1. **Com Docker**:
   - Use o comando:
     ```bash
     cd backend
     docker-compose up
     ```

2. **Sem Docker**:
   - Inicie o backend:
     ```bash
     cd backend
     uvicorn api.main:app --reload
     ```
   - Em outra aba do terminal, inicie o frontend:
     ```bash
     cd frontend
     npm run dev
     ```

cd %TEMP%
git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git
cd pgvector
set "PGROOT=C:\Program Files\PostgreSQL\17"
nmake /F Makefile.win

Executar no console

call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
set "PGROOT=C:\Program Files\PostgreSQL\16"
cd %TEMP%
git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git
cd pgvector
nmake /F Makefile.win
nmake /F Makefile.win install

SELECT * FROM pg_extension WHERE extname = 'vector';
ROLLBACK;
CREATE EXTENSION vector;


## Testando a API

- Acesse a documentação interativa da API em `http://localhost:8000/docs`.

## Estrutura do Projeto

```plaintext
readme.md
.vscode/
backend/
  api/
  database/
  dto/
  models/
  services/
  utils/
frontend/
  src/
    api/
    components/
    interfaces/
```

## Tecnologias Utilizadas

- **Backend**: FastAPI, SQLAlchemy, Alembic
- **Frontend**: ReactJS, Ant Design, Vite
- **Banco de Dados**: PostgreSQL
- **Outros**: Docker, TailwindCSS, OpenAI API

## Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).