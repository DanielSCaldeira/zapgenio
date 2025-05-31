# Zap Genio

## Resumo da Aplicação

Zap Genio é um sistema web completo que integra um backend em Python (API REST), frontend em ReactJS com TailwindCSS e a inteligência da OpenAI para automatizar respostas via WhatsApp. A plataforma permite que clientes (empresas) cadastrem listas de perguntas e respostas, agendem compromissos e consultem históricos de vetores com controle de versões, tudo isso com um sistema de gestão de usuários e permissões por empresa.

## Módulos Principais

1. **Empresas e Usuários**:
   - Controle de login, permissões e gestão de dados por empresa.
   - Permite que cada empresa (cliente) tenha múltiplos usuários.

2. **Listas de Perguntas e Respostas**:
   - Cada lista possui um ID único e é vinculada a uma empresa.
   - As perguntas e respostas são organizadas por lista.
   - Suporte a múltiplas listas por empresa.

3. **Vetorização**:
   - Histórico de vetores gerados ao longo do tempo para cada lista.
   - Indicação do vetor ativo para cálculo de similaridade.

4. **Integração com WhatsApp**:
   - Comparação de mensagens recebidas com vetores ativos para respostas diretas.
   - Integração com ChatGPT para perguntas sem correspondência exata, utilizando um prompt personalizado.

5. **Agenda e Compromissos**:
   - Criação de eventos por usuários.
   - Geração de arquivo `.ics` para cada compromisso.
   - Salvamento de dados na tabela de compromissos.
   - Link para adicionar o compromisso em agendas pessoais (Google Agenda, Outlook, etc.).

6. **Interface Web**:
   - Tela única para visualização, adição, edição e exclusão de perguntas e respostas.
   - Botão para reprocessar vetores e armazenar novas versões.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados no seu ambiente:

- [Docker](https://www.docker.com/)
- [Node.js](https://nodejs.org/) (versão 16 ou superior)
- [npm](https://www.npmjs.com/) ou [yarn](https://yarnpkg.com/)
- [Python](https://www.python.org/) (versão 3.10 ou superior)
- [Poetry](https://python-poetry.org/) (opcional, para gerenciar dependências Python)
- [pgvector-postgresql](https://github.com/pgvector/pgvector)


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

## Configuração do `pgvector`

1. **Baixar e compilar o `pgvector`**:
   ```bash
   call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
   set "PGROOT=C:\Program Files\PostgreSQL\16"
   cd %TEMP%
   git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git
   cd pgvector
   nmake /F Makefile.win
   nmake /F Makefile.win install
   ```

2. **Verificar instalação no PostgreSQL**:
   ```sql
   SELECT * FROM pg_extension WHERE extname = 'vector';
   ```

3. **Criar extensão no banco de dados**:
   ```sql
   CREATE EXTENSION vector;
   ```

## Testando a API

- Acesse a documentação interativa da API no **Swagger UI**:
  - [http://localhost:8000/docs](http://localhost:8000/docs)
  
- Acesse a documentação alternativa no **ReDoc**:
  - [http://localhost:8000/redoc](http://localhost:8000/redoc)

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


ETKA2UPRMJ
XQ2XPSRG9N
8KT9MCEMRD
ZJPWW4P9X8
HD9YEPSJMR
XCC85DSTDW
5EANRC58FH
FGMRS5X9V7
8JSRK8YPAZ
VPXA745657

https://developers.facebook.com/apps/1196756504964148/whatsapp-business

https://loca.lt/mytunnelpassword

https://reactflow.dev/examples/nodes/custom-node