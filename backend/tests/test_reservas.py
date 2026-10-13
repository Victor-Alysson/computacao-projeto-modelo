from datetime import datetime

from app.contexts.reservas.regras import Reserva, ha_conflito


def r(cond, area, h_ini, h_fim):
    return Reserva(cond, area, datetime(2027, 9, 10, h_ini), datetime(2027, 9, 10, h_fim))


def test_horarios_sobrepostos_na_mesma_area_conflitam():
    assert ha_conflito(r(1, 1, 18, 22), [r(1, 1, 20, 23)])


def test_horarios_em_sequencia_nao_conflitam():
    assert not ha_conflito(r(1, 1, 18, 20), [r(1, 1, 20, 23)])


def test_outro_condominio_nao_conflita():
    assert not ha_conflito(r(2, 1, 18, 22), [r(1, 1, 18, 22)])
