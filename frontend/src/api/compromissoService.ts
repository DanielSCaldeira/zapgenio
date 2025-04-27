// src/api/compromissoApi.ts

import axiosInstance from './axiosInstance';

// Tipos TypeScript para os dados de compromissos
export interface Compromisso {
  id: number;
  titulo: string;
  data: string;
}

// Função para buscar todos os compromissos
export const getCompromissos = async (): Promise<Compromisso[]> => {
  const response = await axiosInstance.get('/compromissos');
  return response.data;
};

// Função para criar um novo compromisso
export const createCompromisso = async (compromisso: Compromisso): Promise<Compromisso> => {
  const response = await axiosInstance.post('/compromissos', compromisso);
  return response.data;
};

// Função para atualizar um compromisso
export const updateCompromisso = async (id: number, compromisso: Compromisso): Promise<Compromisso> => {
  const response = await axiosInstance.put(`/compromissos/${id}`, compromisso);
  return response.data;
};

// Função para deletar um compromisso
export const deleteCompromisso = async (id: number): Promise<void> => {
  await axiosInstance.delete(`/compromissos/${id}`);
};
