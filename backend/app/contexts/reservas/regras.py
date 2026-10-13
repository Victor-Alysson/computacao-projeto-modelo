from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Reserva:
    condominio_id: int
    area_id: int
    inicio: datetime
    fim: datetime


def ha_conflito(nova: Reserva, existentes: list[Reserva]) -> bool:
    """Verifica se a nova reserva se sobrepõe a outra da mesma área e condomínio."""
    for r in existentes:
        mesma_area = r.condominio_id == nova.condominio_id and r.area_id == nova.area_id
        sobrepoe = nova.inicio < r.fim and r.inicio < nova.fim
        if mesma_area and sobrepoe:
            return True
    return False
