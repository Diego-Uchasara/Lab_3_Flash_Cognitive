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

Los usuarios normales solicitan un código enviado al correo registrado. Para probar este flujo, inicia sesión con un usuario que tenga un correo válido. Para que funcione debe llenar .env.example con los datos del correo de envio y la contraseña de aplicacion, para que este cumpla la funcion de enviar codigo. Por privacidad no subire mis credenciales de forma publica.

## Detener la aplicación

En la terminal presiona `Ctrl + C` y luego ejecuta:

```powershell
docker compose down
```
