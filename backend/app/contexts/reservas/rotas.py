from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .regras import Reserva, ha_conflito

router = APIRouter()
_reservas: list[Reserva] = []  # em produção: banco de dados, filtrado por condomínio


class PedidoReserva(BaseModel):
    condominio_id: int
    area_id: int
    inicio: datetime
    fim: datetime


@router.post("", status_code=201)
def solicitar_reserva(pedido: PedidoReserva) -> dict:
    nova = Reserva(**pedido.model_dump())
    if ha_conflito(nova, _reservas):
        raise HTTPException(status_code=409, detail="Horário já reservado para esta área.")
    _reservas.append(nova)
    return {"status": "pendente de aprovação do síndico"}
