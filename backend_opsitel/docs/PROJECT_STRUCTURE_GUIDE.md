# Guia de Estructura del Proyecto (Estado Actual)

Esta guia define como organizar el backend modular de forma consistente para seguir creciendo sin regresar a estructura legacy.

## 1. Estructura oficial actual

```text
backend_opsitel/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── bootstrap/
│   │   ├── __init__.py
│   │   └── router.py
│   ├── shared/
│   │   ├── __init__.py
│   │   ├── infrastructure/
│   │   │   ├── __init__.py
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   └── interfaces/
│   │       ├── __init__.py
│   │       └── http/
│   │           ├── __init__.py
│   │           └── deps.py
│   └── modules/
│       ├── __init__.py
│       ├── auth/
│       │   ├── __init__.py
│       │   ├── application/
│       │   │   ├── __init__.py
│       │   │   ├── dto.py
│       │   │   └── use_cases.py
│       │   └── interfaces/
│       │       ├── __init__.py
│       │       └── http/
│       │           ├── __init__.py
│       │           └── v1/
│       │               ├── __init__.py
│       │               └── router.py
│       ├── users/
│       │   ├── __init__.py
│       │   ├── application/
│       │   │   ├── __init__.py
│       │   │   ├── dto.py
│       │   │   └── use_cases.py
│       │   ├── infrastructure/
│       │   │   ├── __init__.py
│       │   │   └── orm_models.py
│       │   └── interfaces/
│       │       ├── __init__.py
│       │       └── http/
│       │           ├── __init__.py
│       │           └── v1/
│       │               ├── __init__.py
│       │               ├── filters.py
│       │               └── router.py
│       ├── inventory/
│       │   ├── __init__.py
│       │   └── README.md
│       ├── payments/
│       │   ├── __init__.py
│       │   └── README.md
│       └── reports/
│           ├── __init__.py
│           └── README.md
├── docs/
│   ├── SCALING_PLAYBOOK.md
│   └── PROJECT_STRUCTURE_GUIDE.md
├── database_opsitel.db
├── pyproject.toml
└── README.md
```

## 2. Que va en cada carpeta

### `app/main.py`
- Punto de entrada de FastAPI.
- Crea la app, registra routers y extensiones (ej. paginacion).
- No debe contener reglas de negocio.

### `app/bootstrap/`
- Composicion de la aplicacion.
- `router.py`: registra todos los routers de modulos.
- Regla: cualquier nuevo modulo con endpoints se registra aqui.

### `app/shared/`
Capas compartidas transversales (no de negocio).

- `shared/infrastructure/database.py`
  - Engine, SessionLocal, Base.
  - Configuracion y utilidades de persistencia global.
- `shared/infrastructure/security.py`
  - Hash de passwords, JWT, helpers de autenticacion.
- `shared/interfaces/http/deps.py`
  - Dependencias HTTP compartidas (ej. `get_db`).

### `app/modules/`
Contiene todos los modulos de negocio (feature-based).
Cada modulo debe ser autocontenido.

#### `app/modules/<modulo>/application/`
- `dto.py`: contratos de entrada/salida de la capa aplicacion.
- `use_cases.py`: casos de uso (servicios de negocio).
- Regla: aqui vive la orquestacion de negocio, no en routers.

#### `app/modules/<modulo>/infrastructure/`
- Adaptadores tecnicos del modulo.
- `orm_models.py`: modelos ORM SQLAlchemy del modulo.
- Futuro: `repositories.py`, `mappers.py`, clientes externos.

#### `app/modules/<modulo>/interfaces/http/v1/`
- `router.py`: endpoints FastAPI.
- `filters.py`: filtros HTTP/consulta del modulo.
- `schemas.py` (opcional): contratos HTTP especificos si difieren de `dto.py`.
- Regla: routers solo validan/orquestan request-response y delegan a `application`.

## 3. Donde van los archivos clave (regla directa)

- Base de datos (conexion/session/base):
  - `app/shared/infrastructure/database.py`
- Seguridad (hash/JWT):
  - `app/shared/infrastructure/security.py`
- Dependencias HTTP comunes:
  - `app/shared/interfaces/http/deps.py`
- Rutas API:
  - `app/modules/<feature>/interfaces/http/v1/router.py`
  - Registro central: `app/bootstrap/router.py`
- Servicios de negocio (casos de uso):
  - `app/modules/<feature>/application/use_cases.py`
- DTOs / Schemas de aplicacion:
  - `app/modules/<feature>/application/dto.py`
- Schemas HTTP (si necesitas separar de DTOs):
  - `app/modules/<feature>/interfaces/http/v1/schemas.py`
- Filtros de consulta por feature:
  - `app/modules/<feature>/interfaces/http/v1/filters.py`
- Modelos ORM:
  - `app/modules/<feature>/infrastructure/orm_models.py`

## 4. Convenciones de nombres de archivos

- `router.py`: siempre para endpoints.
- `use_cases.py`: logica de negocio del modulo.
- `dto.py`: contratos de aplicacion.
- `filters.py`: filtros de busqueda/listado HTTP.
- `orm_models.py`: modelos de tabla SQLAlchemy.
- `repositories.py`: acceso a datos desacoplado (cuando se introduzca).
- `__init__.py`: mantener en todos los paquetes.

## 5. Flujo recomendado de una request

`HTTP router -> use case -> ORM/repository -> DB`

Mas adelante (target completo):

`HTTP router -> use case -> repository port -> repository adapter -> DB`

## 6. Plantilla minima para un nuevo modulo

```text
app/modules/<new_module>/
├── __init__.py
├── application/
│   ├── __init__.py
│   ├── dto.py
│   └── use_cases.py
├── infrastructure/
│   ├── __init__.py
│   └── orm_models.py
└── interfaces/http/v1/
    ├── __init__.py
    ├── router.py
    ├── filters.py          # solo si aplica
    └── schemas.py          # opcional
```

Checklist:
1. Crear estructura del modulo.
2. Implementar DTOs y casos de uso.
3. Crear modelos ORM y/o repositorios.
4. Exponer endpoints en `router.py`.
5. Registrar router en `app/bootstrap/router.py`.
6. Agregar pruebas unitarias e integracion.

## 7. Reglas de dependencia (obligatorias)

- `interfaces` depende de `application`.
- `application` puede depender de `infrastructure` (estado actual), pero objetivo es depender de puertos.
- `shared` no depende de modulos de negocio.
- Evitar imports cruzados directos entre modulos (users -> inventory) sin contrato explicito.

## 8. Anti-patrones prohibidos

- Routers con SQL embebido.
- Logica de negocio en `main.py` o `bootstrap/router.py`.
- Crear una carpeta global `services/` para mezclar todos los modulos.
- Reusar DTOs de un modulo en otro por conveniencia.
- Duplicar reglas de auth/seguridad fuera de `shared/infrastructure/security.py`.

## 9. Archivos que SI deben quedarse en raiz

- `pyproject.toml`: dependencias y configuracion del proyecto.
- `poetry.lock`: lock de dependencias.
- `database_opsitel.db`: archivo SQLite actual del entorno local.
- `README.md`: overview rapido.
- `docs/*`: guias tecnicas y operativas.

## 10. Nota sobre la BD en produccion

Actualmente se usa SQLite local (`database_opsitel.db`).
Si migras a PostgreSQL/MySQL:
- Mantener la configuracion en `app/shared/infrastructure/database.py`.
- No cambiar la ubicacion de casos de uso ni routers.
- Cambiar solo configuracion de engine y migraciones.

