import os

from werkzeug.security import generate_password_hash

from app import db
from app.models.usuario import Usuario


def crear_admin_inicial():
    admin = Usuario.query.filter_by(username="admin").first()
    email = os.getenv("ADMIN_EMAIL", "admin@laboratorio.local")
    password = os.getenv("ADMIN_PASSWORD", "Admin123*")
    if admin is None:
        db.session.add(Usuario(
            nombre="Administrador", username="admin", email=email,
            rol="admin", password_hash=generate_password_hash(password)
        ))
        db.session.commit()
    elif os.getenv("ADMIN_EMAIL"):
        admin.email = email
        admin.password_hash = generate_password_hash(password)
        db.session.commit()

    # Cuenta de evaluación: permite al profesor comprobar el CRUD sin depender
    # del correo personal del estudiante. Los demás usuarios sí usan código.
    if Usuario.query.filter_by(username="profesor").first() is None:
        db.session.add(Usuario(
            nombre="Cuenta de evaluación", username="profesor",
            email="profesor@evaluacion.local", rol="admin",
            password_hash=generate_password_hash("Profesor123*"),
            requiere_codigo=False
        ))
        db.session.commit()
