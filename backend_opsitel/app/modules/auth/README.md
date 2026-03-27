# Modulo: Auth

Autenticacion y autorizacion del CMS.

## Objetivo

Gestionar login, renovacion de token y proteccion de rutas por rol.

## Estado actual

- [x] Ruta implementada: `POST /api/v1/auth/login`.
- [ ] Refresh token.
- [ ] Logout.
- [ ] Dependencia de usuario autenticado (`get_current_user`).
- [ ] Guard de roles (`admin/editor/revisor`).

## Checklist de implementacion de metodos

- [x] `get_token(db, email, password)`.
- [ ] `refresh_token(refresh_token)`.
- [ ] `logout(current_user, refresh_token)`.
- [ ] `validate_active_user(user)`.
- [ ] `require_roles(allowed_roles)`.

## Checklist de rutas

- [x] `POST /api/v1/auth/login`.
- [ ] `POST /api/v1/auth/refresh`.
- [ ] `POST /api/v1/auth/logout`.
- [ ] `GET /api/v1/auth/me`.

## Checklist tecnico

- [ ] Mover `SECRET_KEY` a env (`.env`).
- [ ] Configurar expiracion diferenciada access/refresh.
- [ ] Hash de refresh token en BD o estrategia de revocacion.
- [ ] Manejo uniforme de errores 401/403.
- [ ] Pruebas unitarias y de integracion de auth.

## Criterios de aceptacion

- [ ] Login retorna access + refresh token validos.
- [ ] Refresh invalido retorna 401.
- [ ] Usuario inactivo no puede autenticarse.
- [ ] Rutas protegidas rechazan usuarios sin rol permitido.

