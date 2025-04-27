import React, { useEffect, useState } from 'react';
import { Tabs} from 'antd';
import {  AppleOutlined } from '@ant-design/icons';
import { PerguntaResposta } from './components/PerguntaResposta/PerguntaResposta';
import { getListasPerguntas } from './api/listaPerguntaService.ts ';

interface Pergunta {
  id: number;
  pergunta: string;
  resposta: string;
}

interface ListaPergunta {
  id: number;
  nome: string;
  perguntas?: Pergunta[];
}

const App: React.FC = () => {
  const [listaPerguntas, setListaPerguntas] = useState<ListaPergunta[]>([]); // Estado para armazenar as listas de perguntas

  // Use useEffect para chamar a API quando o componente for montado
  useEffect(() => {
    const fetchListaPerguntas = async () => {
      try {
        const data = await getListasPerguntas(); // Chama a função para obter as listas de perguntas
        setListaPerguntas(data); // Atualiza o estado com os dados da API
      } catch (error) {
        console.error("Erro ao buscar listas de perguntas:", error);
      }
    };

    fetchListaPerguntas(); // Chama a função quando o componente é montado
  }, []); // O array vazio faz com que a requisição aconteça apenas na montagem do componente

  return (
    <>
      <Tabs
        defaultActiveKey="1"
        items={listaPerguntas.map((item) => {
          const id = String(item.id);
          return {
            key: id,
            label: `${item.nome}`,
            children: <>
              <PerguntaResposta perguntas={item.perguntas} ></PerguntaResposta>
            </>,
            icon: <AppleOutlined />,
          };
        })}
      />
    </>
  );
};

export default App;
