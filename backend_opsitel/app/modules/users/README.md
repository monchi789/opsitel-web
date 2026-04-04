# Modulo: Users

Gestion de usuarios del CMS sindical.

## Objetivo

Administrar ciclo de vida de usuarios, roles y estado de activacion.

## Estado actual

- [x] `POST /api/v1/users/`.
- [x] `GET /api/v1/users/`.
- [x] `GET /api/v1/users/{id}`.
- [x] `PATCH /api/v1/users/{id}`.
- [x] `DELETE /api/v1/users/{id}`.
- [ ] `GET /api/v1/users/me`.
- [ ] Borrado logico.
- [ ] Validacion de permisos por rol en endpoints.
1
## Checklist de implementacion de metodos

- [x] `create_user(db, user)`.
- [x] `list_user(db, filters)`.
- [x] `list_user_by_id(db, user_id)`.
- [x] `partial_update_user(db, user_id, user_update)`.
- [x] `eliminate_user(db, user_id)`.
- [ ] `deactivate_user(db, user_id)`.
- [ ] `get_current_user_profile(db, current_user)`.

## Checklist de rutas

- [x] `POST /api/v1/users/`.
- [x] `GET /api/v1/users/`.
- [x] `GET /api/v1/users/{id}`.
- [x] `PATCH /api/v1/users/{id}`.
- [x] `DELETE /api/v1/users/{id}`.
- [ ] `GET /api/v1/users/me`.
- [ ] `PATCH /api/v1/users/{id}/deactivate`.

## Checklist tecnico

- [ ] Cambiar `is_active` de `str` a boolean en ORM.
- [ ] Evitar borrado fisico por defecto.
- [ ] Aplicar permisos por rol en operaciones sensibles.
- [ ] Evitar devolver datos sensibles en responses.
- [ ] Normalizar codigos de error (400/401/403/404/409).
- [ ] Pruebas unitarias e integracion.

## Criterios de aceptacion

- [ ] No se permite email duplicado.
- [ ] Password siempre se guarda hasheado.
- [ ] Usuario desactivado no puede autenticarse.
- [ ] Solo admin puede crear/eliminar usuarios.
- [ ] Listado paginado y filtrable funciona correctamente.

