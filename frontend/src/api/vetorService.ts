// src/api/vetorApi.ts

import axiosInstance from './axiosInstance';

// Tipos TypeScript para vetores
export interface Vetor {
  id: number;
  valor: string;
}

// Função para buscar todos os vetores
export const getVetores = async (): Promise<Vetor[]> => {
  const response = await axiosInstance.get('/vetores');
  return response.data;
};

// Função para criar um novo vetor
export const createVetor = async (vetor: Vetor): Promise<Vetor> => {
  const response = await axiosInstance.post('/vetores', vetor);
  return response.data;
};

// Função para atualizar um vetor
export const updateVetor = async (id: number, vetor: Vetor): Promise<Vetor> => {
  const response = await axiosInstance.put(`/vetores/${id}`, vetor);
  return response.data;
};

// Função para deletar um vetor
export const deleteVetor = async (id: number): Promise<void> => {
  await axiosInstance.delete(`/vetores/${id}`);
};
