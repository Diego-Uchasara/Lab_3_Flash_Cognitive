from app import db


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    rol = db.Column(db.String(20), nullable=False, default="usuario")
    password_hash = db.Column(db.String(255), nullable=False)
    requiere_codigo = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Usuario {self.username}>"
