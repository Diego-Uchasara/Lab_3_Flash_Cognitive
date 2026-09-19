from flask import flash, redirect, render_template, request, session, url_for


class UsuarioController:
    def __init__(self, service):
        self.service = service

    def listar(self):
        return render_template("usuarios/lista.html", usuarios=self.service.listar_usuarios())

    def nuevo(self):
        return render_template("usuarios/formulario.html", usuario=None)

    def crear(self):
        try:
            self.service.crear_usuario(*self._datos_formulario())
            flash("Usuario registrado correctamente", "success")
            return redirect(url_for("usuarios.listar"))
        except ValueError as error:
            flash(str(error), "danger")
            return redirect(url_for("usuarios.nuevo"))

    def editar(self, usuario_id):
        usuario = self.service.obtener_usuario(usuario_id)
        if usuario is None:
            return "Usuario no encontrado", 404
        return render_template("usuarios/formulario.html", usuario=usuario)

    def actualizar(self, usuario_id):
        try:
            self.service.actualizar_usuario(usuario_id, *self._datos_formulario())
            flash("Usuario actualizado correctamente", "success")
        except ValueError as error:
            flash(str(error), "danger")
        return redirect(url_for("usuarios.listar"))

    def eliminar(self, usuario_id):
        if usuario_id == session.get("usuario_id"):
            flash("No puedes eliminar tu propio usuario mientras tienes la sesión abierta", "danger")
        else:
            try:
                self.service.eliminar_usuario(usuario_id)
                flash("Usuario eliminado correctamente", "success")
            except ValueError as error:
                flash(str(error), "danger")
        return redirect(url_for("usuarios.listar"))

    @staticmethod
    def _datos_formulario():
        return (
            request.form.get("nombre"), request.form.get("username"), request.form.get("email"),
            request.form.get("rol"), request.form.get("password")
        )
