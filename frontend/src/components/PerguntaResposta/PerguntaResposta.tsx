import React, { useState } from 'react';
import { Button, Flex } from 'antd';
import { DeleteOutlined } from '@ant-design/icons';
import TextArea from 'antd/es/input/TextArea';


interface Pergunta {
    id: number;
    pergunta: string;
    resposta: string;
}

export const PerguntaResposta = ({ perguntas = [] }: { perguntas?: Pergunta[] }) => {

    const [value] = useState<string>('horizontal');
    const [lista, setperguntas] = useState<Pergunta[]>(perguntas);

    // Função para atualizar a pergunta
    const handleChangePergunta = (id: number, newPergunta: string) => {
        setperguntas((prevState) =>
            prevState.map((item) =>
                item.id === id ? { ...item, pergunta: newPergunta } : item
            )
        );
    };

    // Função para atualizar a resposta
    const handleChangeResposta = (id: number, newResposta: string) => {
        setperguntas((prevState) =>
            prevState.map((item) =>
                item.id === id ? { ...item, resposta: newResposta } : item
            )
        );
    };

    function removerItemResposta(id: number) {
        setperguntas((prevState) => prevState.filter((i) => i.id !== id)
        );
    }

    const adicionarPergunta = () => {
        perguntas.push({
            id: perguntas.length + 1,
            pergunta: '',
            resposta: '',
        });
        setperguntas([...perguntas]);
    };

    return (
        <>
            {lista.map((item) => (
                <Flex gap="middle" vertical key={item.id}>
                    <Flex vertical={value === 'vertical'}>
                        <div style={{ padding: '20px' }}>
                            <label>Pergunta</label>
                            <TextArea
                                value={item.pergunta}
                                onChange={(e) => handleChangePergunta(item.id, e.target.value)}
                                rows={7}
                                placeholder="Digite algo aqui..."
                                style={{ marginBottom: '20px' }}
                            />
                        </div>
                        <div style={{ padding: '20px' }}>
                            <label>Resposta</label>
                            <TextArea
                                value={item.resposta}
                                onChange={(e) => handleChangeResposta(item.id, e.target.value)}
                                rows={7}
                                placeholder="Digite algo aqui..."
                                style={{ marginBottom: '20px' }}
                            />
                        </div>
                        <div style={{ padding: '20px' }}>
                            <Button
                                type="primary"
                                danger
                                icon={<DeleteOutlined />}
                                onClick={() =>
                                    removerItemResposta(item.id)
                                }
                            >
                            </Button>
                        </div>
                    </Flex>
                </Flex>
            ))}
            <Flex>
                <Button type="default" onClick={() => adicionarPergunta()}>
                    Adicionar Pergunta e Resposta
                </Button>
            </Flex>
        </>
    )
}
