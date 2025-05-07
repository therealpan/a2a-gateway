# 🛰️ How to Create Your First A2A Agent

Welcome to A2A Gateway! This guide will walk you through building your first **A2A-ready agent** — an AI service that can communicate with others using the A2A protocol.

You can complete this in under 10 minutes.

---

## 🧰 Prerequisites

Make sure you have:

- Python 3.8+
- `pip install .` from the `a2a-gateway` repo
- A basic understanding of HTTP APIs

---

## 🚀 Step 1: Create Your Agent API

Here's a minimal FastAPI-based agent that simply echoes input:

```python
# echo_agent.py
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class A2ATask(BaseModel):
    input: str

@app.post("/execute")
async def execute(task: A2ATask):
    return {"output": f"ECHO: {task.input}"}
```

Run it:

```bash
uvicorn echo_agent:app --port 5005 --reload
```

Test it:

```bash
curl -X POST http://localhost:5005/execute -H "Content-Type: application/json" -d '{"input": "hello"}'
```

---

## 🧾 Step 2: Create an `agent_card.json`

```json
{
  "id": "echo-agent",
  "name": "Echo Agent",
  "description": "Repeats back the input text.",
  "type": "llm",
  "entrypoint": "http://localhost:5005/execute",
  "capabilities": ["echo"],
  "language": "python",
  "version": "0.1.0",
  "author": "you"
}
```

---

## 📤 Step 3: Publish Your Agent

Use the CLI from `a2a-gateway`:

```bash
a2a-gateway publish --file agent_card.json
```

Your agent is now discoverable by others (locally or in your custom registry).

---

## 📬 Step 4: Send a Task to Your Agent

```bash
a2a-gateway task --to echo-agent --input "Hello A2A"
```

Expected output:

```json
{
  "output": "ECHO: Hello A2A"
}
```

---

## ✅ Next Steps

- Add logic to your agent
- Host it on the web (e.g., Render, Railway)
- Share your agent with the community
- Submit a PR with your card to the A2A Gateway registry

Join the [Discord community](https://discord.gg/3wVy3qs2Zp) to collaborate with other builders 🚀

