// src/api/axiosInstance.ts

import axios, { AxiosInstance } from 'axios';

// Criando a instância do axios com configurações padrões
const axiosInstance: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000/',  // URL do backend, substitua conforme necessário
  headers: {
    'Content-Type': 'application/json',
  },
});

export default axiosInstance;
