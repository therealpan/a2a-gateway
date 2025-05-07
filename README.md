# 🌐 A2A Gateway – Interoperabilità tra agenti AI

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/therealpan/a2a-gateway?style=social)](https://github.com/therealpan/a2a-gateway)
[![Discord](https://img.shields.io/discord/1369570058430316575?label=Join%20us%20on%20Discord&logo=discord&color=5865F2)](https://discord.gg/3wVy3qs2Zp)
[![Made with FastAPI](https://img.shields.io/badge/Built%20with-FastAPI-0f4c81?logo=fastapi)](https://fastapi.tiangolo.com/)
[![CI](https://github.com/therealpan/a2a-gateway/actions/workflows/ci.yml/badge.svg)](https://github.com/therealpan/a2a-gateway/actions/workflows/ci.yml)

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
pip install .
```

### 🧪 Avvia un agente demo

```bash
python demo_agent.py
```

### 🚀 Pubblica il tuo agente

```bash
a2a-gateway publish --file agent_card.json
```

### 📬 Invia un task

```bash
a2a-gateway task --to demo-gpt --input "Traduci: Ciao mondo"
```

---

## 📁 Esempi disponibili

- [`agent_card.json`](./agent_card.json) – card per agenti compatibili A2A
- [`demo_agent.py`](./demo_agent.py) – micro agente FastAPI di test
- [`examples/`](./examples/) – richieste A2A via `curl`, CLI e JSON

---

## 🧾 Esempio di Agent Card

```json
{
  "id": "demo-gpt",
  "name": "Demo GPT Agent",
  "description": "Un semplice agente GPT che traduce testi in inglese",
  "type": "llm",
  "entrypoint": "http://localhost:5001/execute",
  "capabilities": ["translation", "chat"],
  "language": "python",
  "version": "0.1.0",
  "author": "Innoturismo"
}
```

---

## 🤖 Avvia un agente di test

```bash
python demo_agent.py
```

L'agente risponde su `http://localhost:5001/execute` e simula una traduzione.
Perfetto per testare `a2a-gateway publish` e `a2a-gateway task`.

---

## 📎 Esempi pratici

La cartella [`examples/`](./examples/) include:

- `task_via_curl.sh`: invia un task A2A via `curl`
- `task_via_cli.sh`: invia un task A2A con la CLI
- `task.json`: payload esempio per test o automazione

---

## 🧪 Test automatici

Il progetto include test base in `tests/`:

- `test_cli.py`: verifica CLI (`--help`, comandi)
- `test_mocked.py`: test unitari mockati

Per eseguirli:

```bash
pip install pytest
pytest
```

---

## 🧰 Dev Setup

Per contribuire al progetto o lavorare in locale con test, linting e build:

```bash
pip install -r requirements-dev.txt
```

Oppure puoi usare:

```bash
make install
make test
make lint
```

Per lanciare l'agente demo localmente:

```bash
make agent
```

Per creare e pubblicare il pacchetto PyPI:

```bash
make build
make publish
```

---

## 📣 Partecipa alla community

Siamo all'inizio e il tuo contributo può fare la differenza 💡

- ⭐ Fai una star al progetto
- 🛠️ Contribuisci con un agente, una guida o fix
- 🧠 Entra su [Discord](https://discord.gg/3wVy3qs2Zp)
- ✍️ Scrivi articoli o tutorial, li promuoviamo volentieri!

---

## 🧠 Credits

Progetto di **[Innoturismo](https://innoturismo.com)**  
Con il supporto della community AI e ispirato al protocollo [A2A di Google](https://google.github.io/A2A).  
Design open-source, developer-first, federabile.

Distribuito sotto licenza **MIT**.

---

📍 Seguici su [GitHub](https://github.com/therealpan/a2a-gateway) | [a2a.dev](https://a2a.dev) | [Discord](https://discord.gg/3wVy3qs2Zp)
