# Modulo: Content

Gestion de contenidos del CMS sindical (blogs/publicaciones).

## Objetivo

Permitir que usuarios con rol editor/admin publiquen contenido con estandares SEO.

## Checklist de implementacion de metodos

- [ ] `create_post(db, payload, current_user)`.
- [ ] `update_post(db, post_id, payload, current_user)`.
- [ ] `publish_post(db, post_id, current_user)`.
- [ ] `unpublish_post(db, post_id, current_user)`.
- [ ] `delete_post(db, post_id, current_user)` (soft delete).
- [ ] `get_post_by_id(db, post_id)`.
- [ ] `get_post_by_slug(db, slug)`.
- [ ] `list_posts(db, filters, pagination)`.

## Checklist de rutas

- [ ] `POST /api/v1/content/posts`.
- [ ] `PATCH /api/v1/content/posts/{post_id}`.
- [ ] `POST /api/v1/content/posts/{post_id}/publish`.
- [ ] `POST /api/v1/content/posts/{post_id}/unpublish`.
- [ ] `DELETE /api/v1/content/posts/{post_id}`.
- [ ] `GET /api/v1/content/posts`.
- [ ] `GET /api/v1/content/posts/{post_id}`.
- [ ] `GET /api/v1/content/posts/slug/{slug}`.

## Estructura esperada del modulo

```text
content/
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

## Checklist SEO (obligatorio)

- [ ] Campos SEO en ORM y DTOs:
  - [ ] `slug` (unico)
  - [ ] `meta_title`
  - [ ] `meta_description`
  - [ ] `canonical_url`
  - [ ] `og_title`
  - [ ] `og_description`
  - [ ] `og_image`
  - [ ] `twitter_title`
  - [ ] `twitter_description`
  - [ ] `twitter_image`
  - [ ] `excerpt`
- [ ] Validacion de longitud minima/maxima de metadatos.
- [ ] Generacion de `slug` cuando no llegue en payload.
- [ ] Respuesta apta para generar JSON-LD (`BlogPosting`).
- [ ] Filtro por estado para no exponer borradores en publico.

## Criterios de aceptacion

- [ ] Solo `editor/admin` pueden crear, editar y publicar.
- [ ] `revisor` solo lectura.
- [ ] Publicacion en estado `published` exige datos SEO minimos.
- [ ] Listado paginado y filtrable por autor/fecha/estado/region/cargo.
- [ ] Errores HTTP consistentes (400/401/403/404/409).
