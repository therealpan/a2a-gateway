# 🌐 A2A Gateway – Interoperabilità tra agenti AI

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/a2a-gateway/a2a-gateway?style=social)](https://github.com/a2a-gateway/a2a-gateway)
[![Discord](https://img.shields.io/discord/3wVy3qs2Zp?label=Join%20us%20on%20Discord&logo=discord&color=5865F2)](https://discord.gg/3wVy3qs2Zp)
[![Made with FastAPI](https://img.shields.io/badge/Built%20with-FastAPI-0f4c81?logo=fastapi)](https://fastapi.tiangolo.com/)

> **Open-source gateway to make AI agents interoperable using Google's A2A protocol – like Hugging Face, but for agents.**

---

## ✨ Cos'è A2A Gateway?

**A2A Gateway** è un’infrastruttura open-source che rende agenti AI (Claude, GPT, LLM locali) interoperabili tra loro utilizzando il [protocollo A2A di Google](https://google.github.io/A2A).

Come Hugging Face ha unificato l'accesso ai modelli AI, A2A Gateway mira a diventare **lo standard per la collaborazione tra agenti**: pubblici, federati, autonomi e aperti.

---

## 🚀 Cosa puoi fare con A2A Gateway

- 🛰️ Esportare agenti Claude, GPT o custom come **A2A endpoint**
- 📄 Creare e condividere **Agent Card JSON**
- 📦 Usare la **CLI** per gestire task tra agenti
- 🌍 Pubblicare e scoprire agenti via **registry pubblico**
- 🧪 Monitorare attività e task via **dashboard (beta)**

---

## 🛠️ Quickstart

### 🔧 Installa la CLI

```bash
pip install a2a-gateway
```

### 🧪 Avvia un agente demo

```bash
a2a run --agent demo-gpt
```

### 🚀 Pubblica il tuo agente

```bash
a2a publish --file agent_card.json
```

### 📬 Invia un task

```bash
a2a task --to agent-weather --input "Previsioni per domani a Milano?"
```

---

## 📁 Esempi disponibili

- [`agent-gpt-translator`](https://github.com/a2a-gateway/agent-gpt-translator)
- [`agent-claude-summarizer`](https://github.com/a2a-gateway/agent-claude-summarizer)
- [`agent-weather`](https://github.com/a2a-gateway/agent-weather)

🔍 Trova altri agenti nel [Registry pubblico](https://a2a.dev/registry)

---

## 🔧 Cosa include l'MVP

- ✅ Gateway A2A: endpoint standard REST
- ✅ Adapter GPT + Claude
- ✅ CLI Python (`publish`, `task`, `status`)
- ✅ Agent Card JSON + validation
- ✅ Demo agenti funzionanti
- 🔄 Registry (in beta)
- 📊 Dashboard minimale (in sviluppo)

---

## 🧭 Roadmap di sviluppo

| Fase     | Obiettivo                                                             |
|----------|-----------------------------------------------------------------------|
| **Fase 1** | Gateway A2A + Adapter GPT + Demo CLI                                |
| **Fase 2** | Registry pubblico (Supabase), Task manager, CLI completa            |
| **Fase 3** | Dashboard React, API key, monitoraggio task                         |
| **Fase 4** | Governance, reputazione, federation tra gateway                     |

---

## 📣 Partecipa alla community

Siamo all'inizio e il tuo contributo può fare la differenza 💡

- ⭐ Fai una star al progetto
- 🛠️ Contribuisci con un agente, una guida o fix
- 🧠 Entra su [Discord](https://discord.gg/a2a) e proponi idee
- ✍️ Scrivi articoli o tutorial, li promuoviamo volentieri!

---

## 🗺️ Strategia GitHub-first

A2A Gateway è pensato per crescere open, come LangChain o Supabase:

- 📚 Documentazione chiara, CLI pronta e agenti d'esempio
- 📢 Post settimanali su Dev.to, X, Reddit, Medium
- 💬 Discord e GitHub Discussions per supporto e collaborazione
- 🏁 Mini hackathon, challenge e leaderboard pubblica

---

## 🧠 Credits

Progetto di **[Innoturismo](https://innoturismo.com)**  
Con il supporto della community AI e ispirato al protocollo [A2A di Google](https://google.github.io/A2A).  
Design open-source, developer-first, federabile.

Distribuito sotto licenza **MIT**.

---

📍 Seguici su [GitHub](https://github.com/a2a-gateway) | [a2a.dev](https://a2a.dev) | [Discord](https://discord.gg/a2a)
