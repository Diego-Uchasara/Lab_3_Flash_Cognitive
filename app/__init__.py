import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "clave-solo-desarrollo")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///desarrollo.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.home_routes import home_bp
    from app.routes.usuario_routes import usuario_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(usuario_bp)

    with app.app_context():
        from app.models.usuario import Usuario
        from app.services.seed_service import crear_admin_inicial

        db.create_all()
        # Migración ligera para instalaciones que ya tenían la tabla creada.
        db.session.execute(text(
            "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS requiere_codigo BOOLEAN NOT NULL DEFAULT TRUE"
        ))
        db.session.commit()
        crear_admin_inicial()

    return app
