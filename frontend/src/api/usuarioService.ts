// src/api/userApi.ts

import axiosInstance from './axiosInstance';

// Tipos TypeScript para os dados de usuários
export interface User {
  id: number;
  name: string;
  email: string;
}

// Função para buscar todos os usuários
export const getUsers = async (): Promise<User[]> => {
  try {
    const response = await axiosInstance.get('/usuarios');  // Endpoint para listar usuários
    return response.data;
  } catch (error) {
    throw new Error('Erro ao buscar usuários');
  }
};

// Função para criar um novo usuário
export const createUser = async (user: User): Promise<User> => {
  try {
    const response = await axiosInstance.post('/usuarios', user);  // Endpoint para criar usuário
    return response.data;
  } catch (error) {
    throw new Error('Erro ao criar usuário');
  }
};

// Função para atualizar um usuário
export const updateUser = async (id: number, user: User): Promise<User> => {
  try {
    const response = await axiosInstance.put(`/usuarios/${id}`, user);  // Endpoint para atualizar usuário
    return response.data;
  } catch (error) {
    throw new Error('Erro ao atualizar usuário');
  }
};

// Função para deletar um usuário
export const deleteUser = async (id: number): Promise<void> => {
  try {
    await axiosInstance.delete(`/usuarios/${id}`);  // Endpoint para deletar usuário
  } catch (error) {
    throw new Error('Erro ao deletar usuário');
  }
};
