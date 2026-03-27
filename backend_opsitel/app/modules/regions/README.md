# Modulo: Regions

Segmentacion por region para usuarios y contenido.

## Objetivo

Permitir clasificar informacion sindical por region y usarla en filtros y reportes.

## Checklist de implementacion de metodos

- [ ] `create_region(db, payload)`.
- [ ] `update_region(db, region_id, payload)`.
- [ ] `deactivate_region(db, region_id)`.
- [ ] `get_region_by_id(db, region_id)`.
- [ ] `list_regions(db, filters, pagination)`.
- [ ] `assign_user_region(db, user_id, region_id)`.

## Checklist de rutas

- [ ] `POST /api/v1/regions`.
- [ ] `GET /api/v1/regions`.
- [ ] `GET /api/v1/regions/{region_id}`.
- [ ] `PATCH /api/v1/regions/{region_id}`.
- [ ] `PATCH /api/v1/regions/{region_id}/deactivate`.
- [ ] `PATCH /api/v1/regions/{region_id}/users/{user_id}`.

## Estructura esperada del modulo

```text
regions/
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

- [ ] Modelo ORM principal: `Region`.
- [ ] Campos base: `id`, `name`, `code`, `is_active`, `created_at`, `updated_at`.
- [ ] Restriccion de unicidad por `code`.
- [ ] Integracion con `users` y `content` via ids.
- [ ] Registro del router en `app/bootstrap/router.py`.
- [ ] Pruebas unitarias + integracion.

## Criterios de aceptacion

- [ ] No se permiten codigos de region duplicados.
- [ ] Se puede consultar usuarios por region.
- [ ] Se puede consultar contenido por region.
- [ ] Desactivar region no rompe historicos.
