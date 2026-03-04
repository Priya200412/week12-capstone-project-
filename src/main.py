from fastapi import FastAPI, WebSocket
from src.api.routes import router

app = FastAPI(title="TaskFlow API")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "TaskFlow API running"}

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)