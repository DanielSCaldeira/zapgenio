import React, { useState } from 'react';
import { Layout, Row, Col, Table, Button, Input, Space, Dropdown, Menu, Tabs } from 'antd';
import { DeleteOutlined, MoreOutlined } from '@ant-design/icons';

const { Header, Content } = Layout;
const { TabPane } = Tabs;

const App: React.FC = () => {
  const [data, setData] = useState<{ [key: string]: any[] }>({});
  const [currentTab, setCurrentTab] = useState<string>('1');

  // Função para adicionar uma nova pergunta/resposta
  const handleAdd = () => {
    const updatedData = { ...data };
    const list = updatedData[currentTab] || [];

    const newItem = { id: Date.now(), question: '', answer: '' };
    setData({
      ...updatedData,
      [currentTab]: [...list, newItem],
    });
  };

  // Função para editar a pergunta ou a resposta
  const handleEdit = (value: string, column: string, record: any) => {
    const updatedData = { ...data };
    const list = updatedData[currentTab].map((item) =>
      item.id === record.id ? { ...item, [column]: value } : item
    );
    setData({
      ...updatedData,
      [currentTab]: list,
    });
  };

  // Função para excluir uma pergunta/resposta
  const handleDelete = (id: number) => {
    const updatedData = { ...data };
    updatedData[currentTab] = updatedData[currentTab].filter((item) => item.id !== id);
    setData(updatedData);
  };

  // Função para criar novas listas de perguntas/respostas
  const handleTabChange = (key: string) => {
    setCurrentTab(key);
  };

  const handleAddTab = () => {
    const newTabKey = `${Object.keys(data).length + 1}`;
    setData({ ...data, [newTabKey]: [] });
    setCurrentTab(newTabKey);
  };

  // Definindo as colunas da tabela com campos editáveis
  const columns = [
    {
      title: 'Pergunta',
      dataIndex: 'question',
      key: 'question',
      editable: true,
      render: (text: string, record: any) => (
        <Input
          value={text}
          onChange={(e) => handleEdit(e.target.value, 'question', record)}
        />
      ),
    },
    {
      title: 'Resposta',
      dataIndex: 'answer',
      key: 'answer',
      editable: true,
      render: (text: string, record: any) => (
        <Input
          value={text}
          onChange={(e) => handleEdit(e.target.value, 'answer', record)}
        />
      ),
    },
    {
      title: 'Ações',
      key: 'actions',
      render: (_: any, record: any) => (
        <Space size="middle">
          <Button
            icon={<DeleteOutlined />}
            onClick={() => handleDelete(record.id)}
            type="danger"
          />
          <Dropdown
            overlay={
              <Menu>
                <Menu.Item key="delete" onClick={() => handleDelete(record.id)}>
                  Excluir
                </Menu.Item>
              </Menu>
            }
          >
            <Button icon={<MoreOutlined />} />
          </Dropdown>
        </Space>
      ),
    },
  ];

  return (
    <Layout>
      <Header style={{ color: 'white', textAlign: 'center', fontSize: 20 }}>
        Gestão de Perguntas e Respostas - ZapGênio
      </Header>
      <Content style={{ margin: '20px' }}>
        <Row justify="center" gutter={[16, 16]}>
          <Col span={20}>
            <Tabs activeKey={currentTab} onChange={handleTabChange} type="card">
              {Object.keys(data).map((key) => (
                <TabPane tab={`Lista ${key}`} key={key}>
                  <Table
                    columns={columns}
                    dataSource={data[key]}
                    rowKey="id"
                    pagination={false}
                    style={{ marginBottom: 20, width: '100%' }}
                    components={{
                      body: {
                        cell: ({ title, editable, children, ...restProps }: any) => {
                          return (
                            <td {...restProps}>
                              {editable ? (
                                <Input defaultValue={children} />
                              ) : (
                                children
                              )}
                            </td>
                          );
                        },
                      },
                    }}
                    size="large" // Tamanho da tabela maior
                    scroll={{ x: true }} // Permite scroll horizontal
                  />
                  <Button
                    type="primary"
                    onClick={handleAdd}
                    style={{ marginBottom: '16px' }}
                  >
                    Adicionar Pergunta/Resposta
                  </Button>
                </TabPane>
              ))}
              <TabPane tab="Nova Lista" key="new">
                <Button
                  type="primary"
                  onClick={handleAddTab}
                  style={{ marginBottom: '16px' }}
                >
                  Criar Nova Lista
                </Button>
              </TabPane>
            </Tabs>
          </Col>
        </Row>
      </Content>
    </Layout>
  );
};

export default App;
