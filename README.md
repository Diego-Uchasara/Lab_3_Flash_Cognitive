# Laboratorio 3 Flask

Aplicación web con Flask, PostgreSQL y Docker. Incluye inicio de sesión y CRUD de usuarios.

## Requisito

Tener Docker Desktop instalado y abierto.

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

Los usuarios normales solicitan un código enviado al correo registrado. Para enviar códigos reales se configura el archivo privado `.env`.

### Configurar el correo

1. En la carpeta del proyecto, crea el archivo `.env` con este comando:

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
4. Reinicia la aplicación:

   ```powershell
   docker compose up --build -d
   ```

5. Inicia sesión con `admin`. El código llegará al correo definido en `ADMIN_EMAIL`.

`.env` contiene datos privados y no se sube a GitHub. `.env.example` es solo una plantilla pública: se usa para crear `.env` con el comando `Copy-Item .env.example .env`.

## Detener la aplicación

En la terminal presiona `Ctrl + C` y luego ejecuta:

```powershell
docker compose down
```
