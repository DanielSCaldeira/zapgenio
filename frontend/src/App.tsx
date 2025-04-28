import React, { useEffect, useState } from 'react';
import { Input, Tabs, Button, Space } from 'antd';
import { AppleOutlined } from '@ant-design/icons';
import { VwPerguntaResposta } from './components/PerguntaResposta/PerguntaResposta';
import { getListasPerguntas } from './api/ListaPerguntaRespostaService.ts ';
import { ListaPerguntaResposta } from './interfaces/models/ListaPerguntaResposta.interface';

const App: React.FC = () => {
  const [ListaPerguntaRespostas, setListaPerguntaRespostas] = useState<ListaPerguntaResposta[]>([]); // Estado para armazenar as listas de perguntas

  const fetchListaPerguntaRespostas = async () => {
    try {
      if (!ListaPerguntaRespostas.length) {
        let data = await getListasPerguntas();
        data = data.map((item) => ({
          ...item,
          componente: <VwPerguntaResposta perguntas={item.perguntas_respostas} />
        }));

        const defaultItem: ListaPerguntaResposta = {
          id: 1000000,
          descricao: "Componente padrão",
          componente_default: <>
            <Space.Compact style={{ width: '100%' }}>
              <Input defaultValue="Combine input and button" />
              <Button type="primary">Submit</Button>
            </Space.Compact>
          </>,
        };

        data.push(defaultItem); // Adiciona uma nova lista vazia ao final da lista

        setListaPerguntaRespostas(data); // Atualiza o estado com os dados da API
      }
    } catch (error) {
      console.error("Erro ao buscar listas de perguntas:", error);
    }
  };

  // Use useEffect para chamar a API quando o componente for montado
  useEffect(() => {
    fetchListaPerguntaRespostas(); // Chama a função quando o componente é montado
  }, []); // O array vazio faz com que a requisição aconteça apenas na montagem do componente

  return (
    <Tabs
      defaultActiveKey="1"
      items={ListaPerguntaRespostas?.map((item) => {
        const id = String(item.id);
        return {
          key: id,
          label: <>{item.nome_lista ?? item.componente_default}</>,
          children: <>
            {item.componente ?? item.descricao}
          </>,
          icon: <AppleOutlined />,
        };
      })}
    />
  );
};

export default App;
