# Laboratorio 3 Flask

Aplicación web con Flask, PostgreSQL y Docker. Incluye inicio de sesión y CRUD de usuarios.

## Requisito

Tener Docker Desktop instalado y abierto.

## Antes de iniciar: configurar el correo

Se recomienda configurar el correo antes del primer inicio para poder probar el código de validación.

1. En la carpeta del proyecto crea `.env` con:

   ```powershell
   Copy-Item Copy.env .env
   ```

2. Abre `.env` y completa estos datos:

   ```text
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=tu_correo@gmail.com
   SMTP_PASSWORD=tu_contrasena_de_aplicacion
   SMTP_FROM=tu_correo@gmail.com
   ADMIN_EMAIL=tu_correo@gmail.com
   ```

3. En `SMTP_PASSWORD` usa una **contraseña de aplicación de Gmail**, no tu contraseña normal.

Si olvidaste hacerlo, no hay problema: edita `.env` más tarde y reinicia con `docker compose up --build -d`. `.env` contiene datos privados y no se sube a GitHub.

## Ejecutar la aplicación

1. Abre una terminal dentro de la carpeta del proyecto.
2. Ejecuta:

   ```powershell
   docker compose up --build
   ```

3. Espera a que Docker termine de iniciar los servicios.
4. Abre en el navegador:

   ```text
   http://localhost:5000
   ```

## Cuenta para probar el CRUD

```text
Usuario: profesor
Contraseña: Profesor123*
```

Esta cuenta entra directamente al sistema y permite crear, editar y eliminar usuarios.

## Prueba de código por correo

Los usuarios normales solicitan un código enviado al correo registrado. Inicia sesión con `admin`; el código llegará al correo definido en `ADMIN_EMAIL`.

## Detener la aplicación

En la terminal presiona `Ctrl + C` y luego ejecuta:

```powershell
docker compose down
```
