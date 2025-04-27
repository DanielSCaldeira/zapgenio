// src/api/empresaApi.ts

import axiosInstance from './axiosInstance';

// Tipos TypeScript para os dados de empresas
export interface Empresa {
  id: number;
  nome: string;
  cnpj: string;
}

// Função para buscar todas as empresas
export const getEmpresas = async (): Promise<Empresa[]> => {
  const response = await axiosInstance.get('/empresas');
  return response.data;
};

// Função para criar uma nova empresa
export const createEmpresa = async (empresa: Empresa): Promise<Empresa> => {
  const response = await axiosInstance.post('/empresas', empresa);
  return response.data;
};

// Função para atualizar uma empresa
export const updateEmpresa = async (id: number, empresa: Empresa): Promise<Empresa> => {
  const response = await axiosInstance.put(`/empresas/${id}`, empresa);
  return response.data;
};

// Função para deletar uma empresa
export const deleteEmpresa = async (id: number): Promise<void> => {
  await axiosInstance.delete(`/empresas/${id}`);
};
