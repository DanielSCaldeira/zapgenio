// src/api/perguntaRespostaApi.ts

import { PerguntaResposta } from '../interfaces/models/PerguntaResposta.interface';
import axiosInstance from './axiosInstance';

// Tipos TypeScript para perguntas e respostas

// Função para buscar todas as perguntas e respostas
export const getPerguntasRespostas = async (): Promise<PerguntaResposta[]> => {
  const response = await axiosInstance.get('/perguntas-respostas');
  return response.data;
};

// Função para criar uma nova pergunta e resposta
export const createPerguntaResposta = async (perguntaResposta: PerguntaResposta): Promise<PerguntaResposta> => {
  const response = await axiosInstance.post('/perguntas-respostas', perguntaResposta);
  return response.data;
};

// Função para atualizar uma pergunta e resposta
export const updatePerguntaResposta = async (id: number, perguntaResposta: PerguntaResposta): Promise<PerguntaResposta> => {
  const response = await axiosInstance.put(`/perguntas-respostas/${id}`, perguntaResposta);
  return response.data;
};

// Função para deletar uma pergunta e resposta
export const deletePerguntaResposta = async (id: number): Promise<void> => {
  await axiosInstance.delete(`/perguntas-respostas/${id}`);
};
