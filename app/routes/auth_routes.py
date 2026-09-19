from flask import Blueprint

from app.controllers.auth_controller import AuthController
from app.repositories.sqlalchemy_usuario_repository import SQLAlchemyUsuarioRepository
from app.services.email_service import EmailService
from app.services.usuario_service import UsuarioService


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
controller = AuthController(UsuarioService(SQLAlchemyUsuarioRepository()), EmailService())


@auth_bp.route("/login")
def login():
    return controller.formulario_login()


@auth_bp.route("/login", methods=["POST"])
def iniciar_sesion():
    return controller.iniciar_sesion()


@auth_bp.route("/validar-codigo")
def validar_codigo():
    return controller.formulario_codigo()


@auth_bp.route("/validar-codigo", methods=["POST"])
def confirmar_codigo():
    return controller.validar_codigo()


@auth_bp.route("/cancelar-login")
def cancelar_login():
    return controller.cancelar_login()


@auth_bp.route("/logout", methods=["POST"])
def logout():
    return controller.cerrar_sesion()
