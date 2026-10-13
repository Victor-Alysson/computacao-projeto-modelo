"""Ponto de entrada da API. Cada contexto de domínio registra suas rotas aqui."""
from fastapi import FastAPI

from app.contexts.reservas.rotas import router as reservas_router

app = FastAPI(title="Projeto modelo · Diretoria de Computação")
app.include_router(reservas_router, prefix="/reservas", tags=["Reservas"])


@app.get("/saude")
def saude() -> dict:
    return {"status": "ok"}
