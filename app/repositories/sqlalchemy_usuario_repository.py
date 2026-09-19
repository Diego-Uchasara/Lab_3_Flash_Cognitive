from app import db
from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository


class SQLAlchemyUsuarioRepository(UsuarioRepository):
    def obtener_todos(self):
        return Usuario.query.order_by(Usuario.id.desc()).all()

    def obtener_por_id(self, usuario_id):
        return db.session.get(Usuario, usuario_id)

    def obtener_por_username(self, username):
        return Usuario.query.filter_by(username=username).first()

    def obtener_por_email(self, email):
        return Usuario.query.filter_by(email=email).first()

    def crear(self, usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    def actualizar(self, usuario):
        db.session.commit()
        return usuario

    def eliminar(self, usuario):
        db.session.delete(usuario)
        db.session.commit()
