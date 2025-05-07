# 🌐 A2A Gateway – Interoperabilità tra agenti AI

**A2A Gateway** è un'infrastruttura open-source che rende interoperabili agenti AI costruiti su modelli diversi (GPT, Claude, LLM locali) utilizzando il [protocollo A2A](https://google.github.io/A2A) di Google.

Pensalo come il “Hugging Face per agenti”: un modo semplice, aperto e standardizzato per pubblicare, scoprire e far collaborare agenti intelligenti.

---

## ✨ Caratteristiche principali

- 🔄 **Gateway compatibile A2A** per agenti GPT, Claude o custom
- 📄 **Agent Card JSON** per descrivere capacità e interfacce
- 🛰️ **Endpoint standard REST** (`/agent_card`, `/task`, `/status`)
- 📦 **CLI open-source** per pubblicare e interrogare agenti
- 🌍 **Registry pubblico** per esplorare e testare agenti interoperabili
- 🧪 **Dashboard (beta)** per visualizzare task e attività agenti

---

## 🚀 Come funziona

1. Crea un agente con GPT (o Claude, ecc.)
2. Aggiungi un file `agent_card.json` con le sue capacità
3. Pubblica l'agente con `a2a publish`
4. Invia task a qualsiasi altro agente con `a2a task`

✅ Tutto conforme al protocollo [A2A by Google](https://google.github.io/A2A)

---

## 🛠️ Quickstart

### Installa la CLI

```bash
pip install a2a-gateway
