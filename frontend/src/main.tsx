import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import 'antd/dist/reset.css'; // Importando o estilo global do Ant Design
import { ConfigProvider } from 'antd';

ReactDOM.createRoot(document.getElementById('root')).render(
  <ConfigProvider theme={{ mode: 'dark' }}>
    <App />
  </ConfigProvider>
);
