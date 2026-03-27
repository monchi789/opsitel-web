# Modulo: Positions

Gestion de cargos sindicales para segmentacion organizacional.

## Objetivo

Administrar cargos y relacionarlos con usuarios para permisos, filtros y reportes.

## Checklist de implementacion de metodos

- [ ] `create_position(db, payload)`.
- [ ] `update_position(db, position_id, payload)`.
- [ ] `deactivate_position(db, position_id)`.
- [ ] `get_position_by_id(db, position_id)`.
- [ ] `list_positions(db, filters, pagination)`.
- [ ] `assign_user_position(db, user_id, position_id)`.

## Checklist de rutas

- [ ] `POST /api/v1/positions`.
- [ ] `GET /api/v1/positions`.
- [ ] `GET /api/v1/positions/{position_id}`.
- [ ] `PATCH /api/v1/positions/{position_id}`.
- [ ] `PATCH /api/v1/positions/{position_id}/deactivate`.
- [ ] `PATCH /api/v1/positions/{position_id}/users/{user_id}`.

## Estructura esperada del modulo

```text
positions/
├── application/
│   ├── dto.py
│   └── use_cases.py
├── infrastructure/
│   ├── orm_models.py
│   └── repositories.py
└── interfaces/http/v1/
    ├── router.py
    ├── schemas.py
    └── filters.py
```

## Checklist tecnico

- [ ] Modelo ORM principal: `Position`.
- [ ] Campos base: `id`, `name`, `code`, `level`, `is_active`, `created_at`, `updated_at`.
- [ ] Restriccion de unicidad por `code`.
- [ ] Registro del router en `app/bootstrap/router.py`.
- [ ] Relacion con `users` para segmentacion.
- [ ] Pruebas unitarias + integracion.

## Criterios de aceptacion

- [ ] No se permiten codigos de cargo duplicados.
- [ ] Se puede listar usuarios por cargo.
- [ ] Se mantiene historial aunque el cargo se desactive.
- [ ] Permite reportes por cargo en modulo `reports`.
