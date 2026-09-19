import secrets
from datetime import UTC, datetime, timedelta

from flask import flash, redirect, render_template, request, session, url_for


class AuthController:
    def __init__(self, usuario_service, email_service):
        self.usuario_service = usuario_service
        self.email_service = email_service

    def formulario_login(self):
        return render_template("auth/login.html")

    def iniciar_sesion(self):
        usuario = self.usuario_service.autenticar(
            request.form.get("username"), request.form.get("password")
        )
        if usuario is None:
            flash("Usuario o contraseña incorrectos", "danger")
            return redirect(url_for("auth.login"))
        if not usuario.requiere_codigo:
            self._crear_sesion(usuario)
            flash("Acceso de evaluación iniciado", "success")
            return redirect(url_for("usuarios.listar"))
        codigo = f"{secrets.randbelow(1_000_000):06d}"
        session.clear()
        session["usuario_pendiente_id"] = usuario.id
        session["codigo_acceso"] = codigo
        try:
            self.email_service.enviar_codigo(usuario.email, codigo)
        except ValueError as error:
            session.clear()
            flash(str(error), "danger")
            return redirect(url_for("auth.login"))
        session["codigo_expira"] = (datetime.now(UTC) + timedelta(minutes=10)).isoformat()
        flash("Enviamos un código a tu correo. Ingrésalo para continuar.", "info")
        return redirect(url_for("auth.validar_codigo"))

    def formulario_codigo(self):
        if "usuario_pendiente_id" not in session:
            return redirect(url_for("auth.login"))
        return render_template("auth/validar_codigo.html")

    def validar_codigo(self):
        expira = datetime.fromisoformat(session.get("codigo_expira", "1970-01-01T00:00:00+00:00"))
        if datetime.now(UTC) > expira:
            session.clear()
            flash("El código expiró. Inicia sesión nuevamente.", "warning")
            return redirect(url_for("auth.login"))
        if request.form.get("codigo", "").strip() != session.get("codigo_acceso"):
            flash("El código no es válido", "danger")
            return redirect(url_for("auth.validar_codigo"))
        usuario = self.usuario_service.obtener_usuario(session["usuario_pendiente_id"])
        self._crear_sesion(usuario)
        flash("Bienvenido al panel de administración", "success")
        return redirect(url_for("usuarios.listar"))

    def cerrar_sesion(self):
        session.clear()
        flash("Sesión cerrada", "info")
        return redirect(url_for("auth.login"))

    def cancelar_login(self):
        session.clear()
        return redirect(url_for("auth.login"))

    @staticmethod
    def _crear_sesion(usuario):
        session.clear()
        session["usuario_id"] = usuario.id
        session["usuario_nombre"] = usuario.nombre
        session["usuario_rol"] = usuario.rol
