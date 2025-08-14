from fastapi import FastAPI

app = FastAPI()

@app.get("/chat")
def chat(msg: str):
    return {"response": f"You said: {msg}"}

