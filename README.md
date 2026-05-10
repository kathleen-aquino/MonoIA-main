# 🤖 MonoIA — Assistente Financeiro com IA

> Chatbot financeiro inteligente para consulta e gestão de cartão de crédito, com autenticação via CPF e operações CRUD em banco de dados local.

---

## 📋 Visão Geral

O **MonoIA** é um assistente virtual financeiro desenvolvido com Python (Flask) no back-end e HTML/CSS/JS puro no front-end. Ele simula o atendimento de um banco digital, permitindo que usuários autenticados consultem faturas, limites, status do cartão e muito mais — tudo via linguagem natural.

---

## ✨ Funcionalidades

- 🔐 **Login por CPF** — autenticação simples e direta
- 💬 **Chat em linguagem natural** — o sistema classifica a intenção do usuário automaticamente
- 📊 **Consulta de dados** — fatura, limite, bloqueio, parcelas e senha
- ✏️ **Atualização de dados** — alteração de fatura e limite via conversa
- 🗑️ **Exclusão de conta** — com confirmação explícita do usuário
- 🗄️ **Banco de dados SQLite** — leve, local e sem dependências externas

---

## 🛠️ Tecnologias Utilizadas

| Camada      | Tecnologia                        |
|-------------|-----------------------------------|
| Back-end    | Python 3, Flask, Flask-CORS       |
| Banco       | SQLite3                           |
| Front-end   | HTML5, CSS3, JavaScript (Vanilla) |
| Fonte       | Google Fonts — Inter              |

---

## 📁 Estrutura do Projeto

```
MonoIA/
├── app.py          # Servidor Flask — rotas e lógica de classificação de intenção
├── crud.py         # Funções de acesso ao banco (Create, Read, Update, Delete)
├── database.py     # Script de criação e seed do banco de dados
├── clientes.db     # Banco de dados SQLite (gerado pelo database.py)
├── index.html      # Interface do chatbot (front-end)
├── respostas.json  # Respostas padrão por categoria (referência)
└── perguntas.csv   # Base de perguntas para testes
