# Contexto Reservas (exemplo)

**Dono:** Back 2 · **Entregáveis:** B08, B09, B10, F05

## Regras de negócio
- Duas reservas da mesma área não podem ter horários sobrepostos.
- Reserva nasce pendente e só vale depois da aprovação do síndico.
- Toda consulta é filtrada pelo condomínio do usuário.

## Onde está o código
- `backend/app/contexts/reservas/`
- Testes: `backend/tests/test_reservas.py`

## Como testar
```bash
cd backend && pip install -r requirements.txt && pytest
```
