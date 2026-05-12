# 🛡️ Sentinel API

Uma API robusta de monitoramento de URLs desenvolvida como projeto de conclusão de ciclo para o curso de Análise e Desenvolvimento de Sistemas (ADS).

## 🌟 Funcionalidades
- **Monitoramento Autônomo:** Agendador (APScheduler) que testa sites periodicamente.
- **Segurança:** Autenticação via JWT (JSON Web Tokens).
- **Processamento Assíncrono:** Background Tasks para verificação em tempo real sem travar a API.
- **Dashboard de Status:** Rota para acompanhar o funcionamento do agendador.

## 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.x
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Banco de Dados:** SQLite
- **Gestão de Tarefas:** APScheduler

## 📱 Desenvolvimento Mobile
Um diferencial técnico deste projeto é que ele foi inteiramente concebido, desenvolvido e versionado em ambiente mobile Android, utilizando **Pydroid 3** para codificação e **Termux** para gestão de ambiente e Git.

## 🚀 Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Inicie o servidor: `uvicorn app.main:app -- reload

