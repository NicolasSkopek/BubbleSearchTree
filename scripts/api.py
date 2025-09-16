import threading
from fastapi import FastAPI
import uvicorn
from scripts.game import Game

app = FastAPI()

game_instance = Game()

@app.get("/pts")
def get_points():
    return {"points": game_instance.pts}

@app.get("/hp")
def get_hp():
    return {"hp": game_instance.hp}

def start_api():
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

def start_api_thread():
    thread = threading.Thread(target=start_api, daemon=True)
    thread.start()
