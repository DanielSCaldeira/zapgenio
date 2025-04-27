// src/api/listaPerguntaApi.ts

import axiosInstance from './axiosInstance';

interface PerguntaResposta {
  id: number; 
  pergunta: string;
  resposta: string;
}

// Tipos TypeScript para listas de perguntas
export interface ListaPergunta {
  id: number;
  nome: string;
  perguntas_respostas: PerguntaResposta[];
}

// Função para buscar todas as listas de perguntas
export const getListasPerguntas = async (): Promise<ListaPergunta[]> => {
  const response = await axiosInstance.get('/listas-perguntas');
  return response.data;
};

// Função para criar uma nova lista de perguntas
export const createListaPergunta = async (listaPergunta: ListaPergunta): Promise<ListaPergunta> => {
  const response = await axiosInstance.post('/listas-perguntas', listaPergunta);
  return response.data;
};

// Função para atualizar uma lista de perguntas
export const updateListaPergunta = async (id: number, listaPergunta: ListaPergunta): Promise<ListaPergunta> => {
  const response = await axiosInstance.put(`/listas-perguntas/${id}`, listaPergunta);
  return response.data;
};

// Função para deletar uma lista de perguntas
export const deleteListaPergunta = async (id: number): Promise<void> => {
  await axiosInstance.delete(`/listas-perguntas/${id}`);
};
