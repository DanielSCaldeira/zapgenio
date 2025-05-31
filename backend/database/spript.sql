CREATE TABLE IF NOT EXISTS public.empresas
(
    id_empresa integer NOT NULL DEFAULT nextval('empresas_id_empresa_seq'::regclass),
    nome character varying(255) COLLATE pg_catalog."default" NOT NULL,
    cnpj character varying(20) COLLATE pg_catalog."default",
    email_contato character varying(255) COLLATE pg_catalog."default",
    telefone character varying(20) COLLATE pg_catalog."default",
    data_cadastro timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT empresas_pkey PRIMARY KEY (id_empresa)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.empresas
    OWNER to postgres;



CREATE TABLE IF NOT EXISTS public.usuarios
(
    id_usuario integer NOT NULL DEFAULT nextval('usuarios_id_usuario_seq'::regclass),
    id_empresa integer,
    nome character varying(255) COLLATE pg_catalog."default" NOT NULL,
    email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    senha_hash text COLLATE pg_catalog."default" NOT NULL,
    tipo_usuario character varying(20) COLLATE pg_catalog."default" DEFAULT 'comum'::character varying,
    ativo boolean DEFAULT true,
    data_cadastro timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT usuarios_pkey PRIMARY KEY (id_usuario),
    CONSTRAINT usuarios_email_key UNIQUE (email),
    CONSTRAINT usuarios_id_empresa_fkey FOREIGN KEY (id_empresa)
        REFERENCES public.empresas (id_empresa) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.usuarios
    OWNER to postgres;



CREATE TABLE IF NOT EXISTS public.listas_perguntas_respostas
(
    id_lista_pergunta_resposta integer NOT NULL DEFAULT nextval('listas_perguntas_respostas_id_lista_pergunta_resposta_seq'::regclass),
    id_empresa integer,
    nome_lista character varying(255) COLLATE pg_catalog."default",
    descricao text COLLATE pg_catalog."default",
    data_criacao timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT listas_perguntas_respostas_pkey PRIMARY KEY (id_lista_pergunta_resposta),
    CONSTRAINT listas_perguntas_respostas_id_empresa_fkey FOREIGN KEY (id_empresa)
        REFERENCES public.empresas (id_empresa) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.listas_perguntas_respostas
    OWNER to postgres;
-- Index: idx_listas_perguntas_respostas_id_empresa

-- DROP INDEX IF EXISTS public.idx_listas_perguntas_respostas_id_empresa;

CREATE INDEX IF NOT EXISTS idx_listas_perguntas_respostas_id_empresa
    ON public.listas_perguntas_respostas USING btree
    (id_empresa ASC NULLS LAST)
    TABLESPACE pg_default;

-- Table: public.perguntas_respostas

-- DROP TABLE IF EXISTS public.perguntas_respostas;

CREATE TABLE IF NOT EXISTS public.perguntas_respostas
(
    id_pergunta_resposta integer NOT NULL DEFAULT nextval('perguntas_respostas_id_pergunta_resposta_seq'::regclass),
    id_lista_pergunta_resposta integer,
    pergunta text COLLATE pg_catalog."default" NOT NULL,
    resposta text COLLATE pg_catalog."default" NOT NULL,
    data_cadastro timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    ativo boolean DEFAULT false,
    CONSTRAINT perguntas_respostas_pkey PRIMARY KEY (id_pergunta_resposta),
    CONSTRAINT perguntas_respostas_id_lista_pergunta_resposta_fkey FOREIGN KEY (id_lista_pergunta_resposta)
        REFERENCES public.listas_perguntas_respostas (id_lista_pergunta_resposta) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.perguntas_respostas
    OWNER to postgres;


CREATE TABLE IF NOT EXISTS public.vetores
(
    id_vetor integer NOT NULL DEFAULT nextval('vetores_id_vetor_seq'::regclass),
    id_pergunta_resposta integer,
    vetor vector(1536) NOT NULL,
    data_geracao timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    ativo boolean DEFAULT false,
    CONSTRAINT vetores_pkey PRIMARY KEY (id_vetor),
    CONSTRAINT vetores_id_pergunta_resposta_fkey FOREIGN KEY (id_pergunta_resposta)
        REFERENCES public.perguntas_respostas (id_pergunta_resposta) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vetores
    OWNER to postgres;
-- Index: vetores_idx

-- DROP INDEX IF EXISTS public.vetores_idx;

CREATE INDEX IF NOT EXISTS vetores_idx
    ON public.vetores USING ivfflat
    (vetor)
    TABLESPACE pg_default;


CREATE TABLE IF NOT EXISTS public.compromissos
(
    id_compromisso integer NOT NULL DEFAULT nextval('compromissos_id_compromisso_seq'::regclass),
    id_empresa integer,
    titulo character varying(255) COLLATE pg_catalog."default",
    descricao text COLLATE pg_catalog."default",
    data_inicio timestamp without time zone,
    data_fim timestamp without time zone,
    arquivo_ics text COLLATE pg_catalog."default",
    criado_em timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    baixado BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT compromissos_pkey PRIMARY KEY (id_compromisso),
    CONSTRAINT compromissos_id_empresa_fkey FOREIGN KEY (id_empresa)
        REFERENCES public.empresas (id_empresa) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.compromissos
    OWNER to postgres;


CREATE INDEX IF NOT EXISTS idx_perguntas_respostas_id_lista_pergunta_resposta
    ON public.perguntas_respostas USING btree
    (id_lista_pergunta_resposta ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE TABLE credenciais_integracoes (
  id_credencial SERIAL PRIMARY KEY,
  id_empresa INT NOT NULL REFERENCES empresas(id_empresa),
  tipo_integracao INT NOT NULL,
  chave_api TEXT NOT NULL,
  dados_adicionais JSONB,
  webhook_url TEXT,
  phone_number_id VARCHAR(255),
  token_expiracao TIMESTAMP,
  estado_integracao VARCHAR(50),
  ativo BOOLEAN DEFAULT TRUE,
  tentativas_falha INT DEFAULT 0,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  usuario_criador INT REFERENCES usuarios(id_usuario)
);

CREATE TABLE trechos_site (
  id_trecho        SERIAL PRIMARY KEY,
  url              TEXT    NOT NULL,
  titulo_secao     VARCHAR(255),
  conteudo         TEXT    NOT NULL,
  hash_conteudo    VARCHAR(64) UNIQUE NOT NULL,
  ativo            BOOLEAN DEFAULT true,
  criado_em        TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  atualizado_em    TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE trecho_pergunta_resposta (
  id_trecho            INTEGER NOT NULL
    REFERENCES trechos_site(id_trecho)
    ON DELETE CASCADE,
  id_pergunta_resposta INTEGER NOT NULL
    REFERENCES perguntas_respostas(id_pergunta_resposta)
    ON DELETE CASCADE,
  PRIMARY KEY (id_trecho, id_pergunta_resposta)
);

-- Tabela etapa
CREATE TABLE etapa (
    id SERIAL PRIMARY KEY,
    id_empresa INTEGER NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    CONSTRAINT fk_empresa_etapa FOREIGN KEY (id_empresa) REFERENCES empresas (id_empresa) ON DELETE CASCADE
);

-- Tabela botoes_etapas
CREATE TABLE botoes_etapas (
    id SERIAL PRIMARY KEY,
    id_etapa INTEGER NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    CONSTRAINT fk_etapa_botoes FOREIGN KEY (id_etapa) REFERENCES etapa (id) ON DELETE CASCADE
);

-- Tabela etapa_seguinte
CREATE TABLE etapa_seguinte (
    id SERIAL PRIMARY KEY,
    id_etapa INTEGER NOT NULL,
    id_botao INTEGER NOT NULL,
    id_etapa_seguinte INTEGER NOT NULL,
    CONSTRAINT fk_etapa_seguinte_etapa FOREIGN KEY (id_etapa) REFERENCES etapa (id) ON DELETE CASCADE,
    CONSTRAINT fk_etapa_seguinte_botao FOREIGN KEY (id_botao) REFERENCES botoes_etapas (id) ON DELETE CASCADE,
    CONSTRAINT fk_etapa_seguinte_etapa_seguinte FOREIGN KEY (id_etapa_seguinte) REFERENCES etapa (id) ON DELETE CASCADE
);