# 🌐 A2A Gateway – Interoperability for AI Agents

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/therealpan/a2a-gateway?style=social)](https://github.com/therealpan/a2a-gateway)
[![Discord](https://img.shields.io/discord/1369570058430316575?label=Join%20us%20on%20Discord&logo=discord&color=5865F2)](https://discord.gg/3wVy3qs2Zp)
[![Made with FastAPI](https://img.shields.io/badge/Built%20with-FastAPI-0f4c81?logo=fastapi)](https://fastapi.tiangolo.com/)
[![CI](https://github.com/therealpan/a2a-gateway/actions/workflows/ci.yml/badge.svg)](https://github.com/therealpan/a2a-gateway/actions/workflows/ci.yml)

> **An open-source gateway to make AI agents interoperable using Google's A2A protocol – like Hugging Face, but for agents.**

---

## ✨ What is A2A Gateway?

**A2A Gateway** is an open-source infrastructure that enables AI agents (Claude, GPT, local LLMs, etc.) to interoperate using the [A2A protocol by Google](https://google.github.io/A2A).

Just as Hugging Face unified access to AI models, A2A Gateway aims to become the **standard for collaboration among agents** – public, federated, autonomous, and open.

But it is more than just a protocol implementation.

A2A Gateway is also a shared space — an open **agora** — for everyone interested in **agentic AI interoperability** to:

- 💬 Discuss standards and best practices
- 🤝 Cooperate on toolkits, adapters, and orchestrators
- 🚀 Contribute agents, demos, ideas, and feedback
- 🌱 Grow a federated ecosystem that is transparent, ethical, and developer-first

If you're building, experimenting, or just curious — you're welcome in the conversation. Join us and shape the interoperable future of AI agents.

---

## 🚀 What You Can Do with A2A Gateway

- 🛰️ Export Claude, GPT, or custom agents as **A2A endpoints**
- 📄 Create and share **Agent Card JSONs**
- 📦 Use the **CLI** to manage tasks between agents
- 🌍 Publish and discover agents via a **public registry**
- 🧪 Monitor activities and tasks via a **dashboard (beta)**

---

## 🛠️ Quickstart

### 📚 Docs & Guides

A2A Gateway is built to be developer-first, lightweight, and interoperable by design.  
Whether you're building your first agent, federating across services, or integrating LangChain — we've got step-by-step guides to get you there fast.

Explore the core documentation to get started:

- 🛰️ **[How to Create Your First A2A Agent](docs/how_to_create_your_first_a2a_agent.md)**  
  Build a working agent with FastAPI and expose it via A2A in 10 minutes.

- 🤝 **[How to Federate with Other Agents](docs/how_to_federate_with_other_agents.md)**  
  Discover, import, and route tasks across trusted agent networks.

- 🔌 **[How to Publish a LangChain Adapter](docs/how_to_publish_langchain_adapter.md)**  
  Wrap LangChain LLMs or chains and connect them to the A2A ecosystem.

→ 📖 [View full documentation index](docs/docs_index.md)


### 🔧 Install the CLI

```bash
pip install .
```

### 🧪 Run a demo agent

```bash
python demo_agent.py
```

### 🚀 Publish your agent

```bash
a2a-gateway publish --file agent_card.json
```

### 📬 Send a task

```bash
a2a-gateway task --to demo-gpt --input "Translate: Hello world"
```

---

## 📁 Available Examples

- [`agent_card.json`](./agent_card.json) – A2A-compliant agent card
- [`demo_agent.py`](./demo_agent.py) – FastAPI test agent
- [`examples/`](./examples/) – A2A requests via `curl`, CLI and JSON

---

## 🧾 Sample Agent Card

```json
{
  "id": "demo-gpt",
  "name": "Demo GPT Agent",
  "description": "A simple GPT agent that translates text into English",
  "type": "llm",
  "entrypoint": "http://localhost:5001/execute",
  "capabilities": ["translation", "chat"],
  "language": "python",
  "version": "0.1.0",
  "author": "Innoturismo"
}
```

---

## 🤖 Run a Test Agent

```bash
python demo_agent.py
```

The agent responds at `http://localhost:5001/execute` and simulates a translation.
Perfect for testing `a2a-gateway publish` and `a2a-gateway task`.

---

## 📎 Practical Examples

The [`examples/`](./examples/) folder includes:

- `task_via_curl.sh`: send an A2A task via `curl`
- `task_via_cli.sh`: send a task using the CLI
- `task.json`: sample payload for testing or automation

---

## 🧪 Automated Tests

The project includes basic tests under `tests/`:

- `test_cli.py`: tests CLI (`--help`, commands)
- `test_mocked.py`: unit tests using mocks

To run tests:

```bash
pip install pytest
pytest
```

---

## 🧰 Dev Setup

To contribute or work locally with tests, linting and builds:

```bash
pip install -r requirements-dev.txt
```

Or use:

```bash
make install
make test
make lint
```

To run the demo agent locally:

```bash
make agent
```

To build and publish the PyPI package:

```bash
make build
make publish
```

---

## 📣 Join the Community

We're just getting started – your contribution can make a real difference 💡

- ⭐ Star the project
- 🛠️ Submit a custom agent, guide or bugfix
- 🧠 Join the [Discord community](https://discord.gg/3wVy3qs2Zp)
- ✍️ Write articles or tutorials – we’ll amplify them!

---

## 🏷️ A2A Gateway Compatibility Badges

If your agent or project is compatible with the A2A Gateway protocol, you can proudly show it using one of our official badges!

### 🚀 A2A Ready

```markdown
![A2A Ready](https://img.shields.io/badge/A2A_READY-%F0%9F%9A%80-blueviolet?style=for-the-badge&logo=protocolsio&logoColor=white)
```

[![A2A Ready](https://img.shields.io/badge/A2A_READY-%F0%9F%9A%80-blueviolet?style=for-the-badge&logo=protocolsio&logoColor=white)](#)

---

### 🧠 Interoperable Agent

```markdown
![Interop Agent](https://img.shields.io/badge/Interoperable_Agent-%E2%9C%94%EF%B8%8F-0f4c81?style=for-the-badge&logo=linktree&logoColor=white)
```

![Interop Agent](https://img.shields.io/badge/Interoperable_Agent-%E2%9C%94%EF%B8%8F-0f4c81?style=for-the-badge&logo=linktree&logoColor=white)

---

### 👷 Developer-First

```markdown
![Developer First](https://img.shields.io/badge/Developer--First-%E2%9C%A8-2aa198?style=for-the-badge&logo=github)
```

![Developer First](https://img.shields.io/badge/Developer--First-%E2%9C%A8-2aa198?style=for-the-badge&logo=github)

---

### 🧪 A2A Experimental

```markdown
![A2A Experimental](https://img.shields.io/badge/A2A_Experimental-%F0%9F%94%8E-yellow?style=for-the-badge&logo=flask&logoColor=black)
```

![A2A Experimental](https://img.shields.io/badge/A2A_Experimental-%F0%9F%94%8E-yellow?style=for-the-badge&logo=flask&logoColor=black)

---

### 🤖 Hugging Face for Agents

```markdown
![HF for Agents](https://img.shields.io/badge/HuggingFace_for_Agents-%F0%9F%A4%96-orange?style=for-the-badge)
```

![HF for Agents](https://img.shields.io/badge/HuggingFace_for_Agents-%F0%9F%A4%96-orange?style=for-the-badge)

---

### 📌 How to Use

Add any of these snippets to your project's `README.md`:

```markdown
[![A2A Ready](https://img.shields.io/badge/A2A_READY-%F0%9F%9A%80-blueviolet?style=for-the-badge&logo=protocolsio&logoColor=white)](https://github.com/therealpan/a2a-gateway)
```

Replace the image or color to best match your brand, or ask us on Discord for a custom badge!

Have an A2A-compatible agent? Open a pull request to be featured in the registry 🛰️

---

## 🧠 Credits

Project initiated by **[Pan](https://github.com/therealpan)** and the **A2A enthusiast crew**, with support from **[Harmonya](https://harmonya.online)**.
With support from the AI community and inspired by [Google’s A2A protocol](https://google.github.io/A2A).  
Open-source, developer-first, federated design.

Licensed under **MIT**.

---

📍 Follow us on [GitHub](https://github.com/therealpan/a2a-gateway) | [Discord](https://discord.gg/3wVy3qs2Zp)
