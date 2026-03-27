# Backend CMS - Sindicato Opsitel

Backend modular para el CMS del sindicato Opsitel.

## Objetivo del sistema

El sistema debe cubrir estos dominios:

- Gestion de usuarios.
- Autenticacion y control de acceso por rol.
- Gestion de contenido tipo blog (publicaciones de editores).
- Segmentacion por region.
- Segmentacion por cargo.
- Reportes institucionales por region, cargo y contenido.

## Estructura actual

```text
backend_opsitel/
├── app/
│   ├── main.py
│   ├── bootstrap/
│   │   └── router.py
│   ├── shared/
│   │   ├── infrastructure/
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   └── interfaces/http/
│   │       └── deps.py
│   └── modules/
│       ├── auth/
│       ├── users/
│       ├── content/
│       ├── regions/
│       ├── positions/
│       └── reports/
├── docs/
├── database_opsitel.db
└── pyproject.toml
```

## Donde va cada tipo de archivo

- Conexion BD y sesion: `app/shared/infrastructure/database.py`.
- Seguridad (hash/JWT): `app/shared/infrastructure/security.py`.
- Dependencias HTTP comunes: `app/shared/interfaces/http/deps.py`.
- Rutas por modulo: `app/modules/<feature>/interfaces/http/v1/router.py`.
- Casos de uso (servicios): `app/modules/<feature>/application/use_cases.py`.
- DTOs/schemas de aplicacion: `app/modules/<feature>/application/dto.py`.
- Filtros HTTP: `app/modules/<feature>/interfaces/http/v1/filters.py`.
- ORM por modulo: `app/modules/<feature>/infrastructure/orm_models.py`.
- Registro central de routers: `app/bootstrap/router.py`.

## Modulos y estado

- `auth`: implementado de forma basica; faltan endpoints y controles.
- `users`: implementado base CRUD; faltan controles de negocio.
- `content`: creado con checklist; pendiente implementacion completa con SEO.
- `regions`: creado con checklist; pendiente implementacion.
- `positions`: creado con checklist; pendiente implementacion.
- `reports`: creado con checklist; pendiente implementacion.

## Checklists por modulo

- `app/modules/auth/README.md`
- `app/modules/users/README.md`
- `app/modules/content/README.md`
- `app/modules/regions/README.md`
- `app/modules/positions/README.md`
- `app/modules/reports/README.md`

## Faltantes detectados hoy (prioridad)

### Auth
- [ ] Mover `SECRET_KEY` a variable de entorno.
- [ ] Implementar `POST /api/v1/auth/refresh`.
- [ ] Implementar `POST /api/v1/auth/logout`.
- [ ] Validar usuario activo antes de emitir tokens.
- [ ] Agregar dependencia `get_current_user` para proteger rutas privadas.

### Users
- [ ] Cambiar borrado fisico por borrado logico (`is_active=false`).
- [ ] Normalizar `is_active` en BD a boolean real.
- [ ] Validar permisos por rol para `create/update/delete`.
- [ ] Agregar endpoint `GET /api/v1/users/me`.
- [ ] Evitar exponer campos sensibles en todas las respuestas.

## Requisito SEO para blogs (obligatorio)

El modulo `content` debe incluir:

- [ ] `slug` unico por publicacion.
- [ ] `meta_title` y `meta_description`.
- [ ] `canonical_url`.
- [ ] Open Graph: `og_title`, `og_description`, `og_image`.
- [ ] Twitter card basica.
- [ ] JSON-LD para `BlogPosting`.
- [ ] Campo `excerpt` para listados.
- [ ] Sitemap y robots listos para integracion.

## Flujo recomendado

`router -> use_case -> repository/orm -> database`
