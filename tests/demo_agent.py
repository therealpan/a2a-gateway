# demo_agent.py
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/execute")
async def handle_task(request: Request):
    body = await request.json()
    input_text = body.get("input", "")
    return {
        "response": f"Translated to English: '{input_text}' (fake translation)",
        "status": "done"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
