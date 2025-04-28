// src/api/ListaPerguntaRespostaApi.ts

import axiosInstance from './axiosInstance';

export interface PerguntaResposta {
  id: number;
  pergunta: string;
  resposta: string;
}

export interface ListaPerguntaResposta {
  nome_lista: string;
  descricao: string;
  id_empresa: number;
  perguntas_respostas: PerguntaResposta[];
  id: number;
}

// Função para buscar todas as listas de perguntas
export const getListasPerguntas = async (): Promise<ListaPerguntaResposta[]> => {
  const response = await axiosInstance.get('/listas-perguntas-respostas');
  return response.data;
};

// Função para criar uma nova lista de perguntas
export const createListaPerguntaResposta = async (ListaPerguntaResposta: ListaPerguntaResposta): Promise<ListaPerguntaResposta> => {
  const response = await axiosInstance.post('/listas-perguntas-respostas', ListaPerguntaResposta);
  return response.data;
};

// Função para atualizar uma lista de perguntas
export const updateListaPerguntaResposta = async (id: number, ListaPerguntaResposta: ListaPerguntaResposta): Promise<ListaPerguntaResposta> => {
  const response = await axiosInstance.put(`/listas-perguntas-respostas/${id}`, ListaPerguntaResposta);
  return response.data;
};

// Função para deletar uma lista de perguntas
export const deleteListaPerguntaResposta = async (id: number): Promise<void> => {
  await axiosInstance.delete(`/listas-perguntas-respostas/${id}`);
};
