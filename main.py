from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI(title="SCAEB Backend", version="1.0.0")

# Modelo de datos de un caso
class Caso(BaseModel):
    caso_id: str
    perito_id: str
    fecha_captura: str
    ubicacion: str
    clasificacion: dict
    modo_captura: str
    latencia_ms: int
    imagen_hash: str

# Almacenamiento temporal en memoria
casos_recibidos = []

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "mensaje": "Servidor SCAEB activo",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/sync")
def sincronizar_caso(caso: Caso):
    casos_recibidos.append(caso.dict())
    return {
        "status": "ok",
        "mensaje": "Sincronización exitosa",
        "caso_id": caso.caso_id,
        "total_casos": len(casos_recibidos)
    }

@app.get("/casos")
def listar_casos():
    return {
        "total": len(casos_recibidos),
        "casos": casos_recibidos
    }
