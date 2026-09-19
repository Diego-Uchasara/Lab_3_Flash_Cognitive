from functools import wraps

from flask import Blueprint, flash, redirect, session, url_for

from app.controllers.usuario_controller import UsuarioController
from app.repositories.sqlalchemy_usuario_repository import SQLAlchemyUsuarioRepository
from app.services.usuario_service import UsuarioService


usuario_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")
controller = UsuarioController(UsuarioService(SQLAlchemyUsuarioRepository()))


def requiere_login(vista):
    @wraps(vista)
    def protegida(*args, **kwargs):
        if not session.get("usuario_id"):
            flash("Inicia sesión para acceder al panel", "warning")
            return redirect(url_for("auth.login"))
        return vista(*args, **kwargs)
    return protegida


@usuario_bp.route("/")
@requiere_login
def listar():
    return controller.listar()


@usuario_bp.route("/nuevo")
@requiere_login
def nuevo():
    return controller.nuevo()


@usuario_bp.route("/crear", methods=["POST"])
@requiere_login
def crear():
    return controller.crear()


@usuario_bp.route("/<int:usuario_id>/editar")
@requiere_login
def editar(usuario_id):
    return controller.editar(usuario_id)


@usuario_bp.route("/<int:usuario_id>/actualizar", methods=["POST"])
@requiere_login
def actualizar(usuario_id):
    return controller.actualizar(usuario_id)


@usuario_bp.route("/<int:usuario_id>/eliminar", methods=["POST"])
@requiere_login
def eliminar(usuario_id):
    return controller.eliminar(usuario_id)
