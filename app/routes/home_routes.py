from flask import Blueprint, redirect, session, url_for


home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    return redirect(url_for("usuarios.listar" if session.get("usuario_id") else "auth.login"))
