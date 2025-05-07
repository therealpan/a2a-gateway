# 🤝 How to Federate with Other A2A Agents

Federation means your agent can *discover*, *trust*, and *collaborate* with other agents using the A2A protocol.

This guide shows how to set up local or public agent federation using A2A Gateway.

---

## 🌐 What Is Federation?

In A2A, federation means:

- Agents can **share metadata** through agent cards
- You can **import cards** from trusted registries
- Agents can **route tasks** to each other via their `entrypoint`

Think of it as DNS + Web + Microservices… but for AI agents.

---

## 📁 Step 1: Import Other Agents' Cards

To federate with agents, you need their `agent_card.json`.  
These can come from:

- GitHub
- Your internal network
- Public A2A registry (coming soon)

### Example:

```bash
wget https://example.com/agents/translator-card.json -O agents/translator.json
```

You can also clone cards into a shared folder.

---

## 🗂️ Step 2: Register the Cards in Your Local Directory

Organize imported agents in a folder like:

```
a2a-gateway/
├── agents/
│   ├── echo-agent.json
│   ├── translator.json
```

Ensure your CLI or gateway loads cards from `./agents`.

---

## 🧪 Step 3: Route a Task to a Federated Agent

With the card available, use the CLI:

```bash
a2a-gateway task --to translator --input "Hello" --meta '{"lang": "fr"}'
```

This sends the task to the external agent’s `entrypoint`.

---

## 🔐 Step 4: Handle Trust and Security

You can add trust metadata in the card:

```json
"trust": {
  "source": "https://github.com/org/verified-agents",
  "score": 0.92,
  "verified": true
}
```

⚠️ Use secure `https` endpoints and authentication headers when needed.

---

## 🚀 Step 5: Contribute to the Ecosystem

Help others federate with you:

- Host your agent card at a stable public URL
- Include a `README.md` with usage instructions
- Add your agent to the public registry (coming soon)
- Share on Discord or in the `#introduce-your-agent` channel

---

## ✅ Done!

You're now part of the A2A agent mesh 🌍

Start federating, exploring and collaborating — one task at a time.

Need help? Jump into [our Discord](https://discord.gg/3wVy3qs2Zp)
