import { JSX, ReactNode } from 'react';
import { PerguntaResposta } from './PerguntaResposta.interface';

export interface ListaPerguntaResposta {
  id: number;
  nome_lista?: string;
  descricao?: string;
  id_empresa?: number;
  perguntas_respostas?: PerguntaResposta[];
  componente?: ReactNode | JSX.Element; 
  componente_default?: ReactNode | JSX.Element; 
}
