import { PerguntaResposta } from './PerguntaResposta.interface';

export interface ListaPergunta {
  nome_lista: string;
  descricao: string;
  id_empresa: number;
  perguntas_respostas: PerguntaResposta[];
  id: number;
}
