# Modulo: Reports

Reportes del CMS por usuarios, contenido, regiones y cargos.

## Objetivo

Entregar consultas operativas y analiticas para toma de decisiones sindicales.

## Checklist de implementacion de metodos

- [ ] `get_users_summary(db, filters)`.
- [ ] `get_content_summary(db, filters)`.
- [ ] `get_content_by_region(db, region_id, filters)`.
- [ ] `get_content_by_position(db, position_id, filters)`.
- [ ] `export_report_csv(data)`.
- [ ] `export_report_xlsx(data)`.

## Checklist de rutas

- [ ] `GET /api/v1/reports/users/summary`.
- [ ] `GET /api/v1/reports/content/summary`.
- [ ] `GET /api/v1/reports/content/by-region/{region_id}`.
- [ ] `GET /api/v1/reports/content/by-position/{position_id}`.
- [ ] `GET /api/v1/reports/export/csv`.
- [ ] `GET /api/v1/reports/export/xlsx`.

## Estructura esperada del modulo

```text
reports/
├── application/
│   ├── dto.py
│   └── use_cases.py
├── infrastructure/
│   ├── repositories.py
│   └── exporters.py
└── interfaces/http/v1/
    ├── router.py
    ├── schemas.py
    └── filters.py
```

## Checklist tecnico

- [ ] Filtros por rango de fecha, region, cargo, autor, estado.
- [ ] Paginacion en listados de alto volumen.
- [ ] Exportacion sin bloquear peticiones largas.
- [ ] Registro del router en `app/bootstrap/router.py`.
- [ ] Pruebas de integracion sobre agregaciones.

## Criterios de aceptacion

- [ ] Resultados consistentes con datos reales de BD.
- [ ] Performance aceptable con volumen medio/alto.
- [ ] Exportaciones validas y descargables.
- [ ] Rutas protegidas por permisos de rol.
