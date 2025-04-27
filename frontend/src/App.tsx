import React, { useEffect, useState } from 'react';
import { Tabs } from 'antd';
import { AppleOutlined } from '@ant-design/icons';
import { VwPerguntaResposta } from './components/PerguntaResposta/PerguntaResposta';
import { getListasPerguntas } from './api/listaPerguntaService.ts ';
import { ListaPergunta } from './interfaces/models/ListaPergunta.interface';


const App: React.FC = () => {
  const [listaPerguntas, setListaPerguntas] = useState<ListaPergunta[]>([]); // Estado para armazenar as listas de perguntas

  const fetchListaPerguntas = async () => {
    try {
      if (!listaPerguntas.length) {
        const data = await getListasPerguntas(); // Chama a função para obter as listas de perguntas
        console.log(data); // Loga os dados recebidos
        setListaPerguntas(data); // Atualiza o estado com os dados da API
      }
    } catch (error) {
      console.error("Erro ao buscar listas de perguntas:", error);
    }
  };

  // Use useEffect para chamar a API quando o componente for montado
  useEffect(() => {
    fetchListaPerguntas(); // Chama a função quando o componente é montado
  }, []); // O array vazio faz com que a requisição aconteça apenas na montagem do componente

  return (
      <Tabs
        defaultActiveKey="1"
        items={listaPerguntas.map((item) => {
          const id = String(item.id);
          return {
            key: id,
            label: `${item.nome_lista}`,
            children: <>
              <VwPerguntaResposta perguntas={item.perguntas_respostas} ></VwPerguntaResposta>
            </>,
            icon: <AppleOutlined />,
          };
        })}
      />
  );
};

export default App;
