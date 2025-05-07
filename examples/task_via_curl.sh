# examples/task_via_curl.sh

# Invia un task a un agente A2A usando curl
curl -X POST http://localhost:8000/task \
     -H "Content-Type: application/json" \
     -d '{
       "agent_id": "demo-gpt",
       "input": "Traduci: buongiorno"
     }'
