import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "TradeMind AI est en cours d'exécution 🚀"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Récupère la variable PORT de Render
    uvicorn.run(app, host="0.0.0.0", port=port)
