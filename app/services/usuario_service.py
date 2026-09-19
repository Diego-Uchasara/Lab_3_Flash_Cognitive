from werkzeug.security import check_password_hash, generate_password_hash

from app.models.usuario import Usuario


class UsuarioService:
    ROLES_VALIDOS = {"admin", "usuario"}

    def __init__(self, repository):
        self.repository = repository

    def listar_usuarios(self):
        return self.repository.obtener_todos()

    def obtener_usuario(self, usuario_id):
        return self.repository.obtener_por_id(usuario_id)

    def autenticar(self, username, password):
        usuario = self.repository.obtener_por_username((username or "").strip())
        if usuario is None or not check_password_hash(usuario.password_hash, password or ""):
            return None
        return usuario

    def crear_usuario(self, nombre, username, email, rol, password):
        self._validar(nombre, username, email, rol, password)
        if self.repository.obtener_por_username(username.strip()):
            raise ValueError("El nombre de usuario ya está registrado")
        if self.repository.obtener_por_email(email.strip().lower()):
            raise ValueError("El correo ya está registrado")
        usuario = Usuario(
            nombre=nombre.strip(), username=username.strip(), email=email.strip().lower(),
            rol=rol, password_hash=generate_password_hash(password)
        )
        return self.repository.crear(usuario)

    def actualizar_usuario(self, usuario_id, nombre, username, email, rol, password):
        usuario = self.repository.obtener_por_id(usuario_id)
        if usuario is None:
            raise ValueError("Usuario no encontrado")
        self._validar(nombre, username, email, rol, password, password_opcional=True)
        otro_username = self.repository.obtener_por_username(username.strip())
        otro_email = self.repository.obtener_por_email(email.strip().lower())
        if otro_username and otro_username.id != usuario.id:
            raise ValueError("El nombre de usuario ya está registrado")
        if otro_email and otro_email.id != usuario.id:
            raise ValueError("El correo ya está registrado")
        usuario.nombre, usuario.username = nombre.strip(), username.strip()
        usuario.email, usuario.rol = email.strip().lower(), rol
        if password:
            usuario.password_hash = generate_password_hash(password)
        return self.repository.actualizar(usuario)

    def eliminar_usuario(self, usuario_id):
        usuario = self.repository.obtener_por_id(usuario_id)
        if usuario is None:
            raise ValueError("Usuario no encontrado")
        self.repository.eliminar(usuario)

    def _validar(self, nombre, username, email, rol, password, password_opcional=False):
        if not (nombre or "").strip() or not (username or "").strip() or not (email or "").strip():
            raise ValueError("Nombre, usuario y correo son obligatorios")
        if "@" not in email:
            raise ValueError("El correo no es válido")
        if rol not in self.ROLES_VALIDOS:
            raise ValueError("El rol no es válido")
        if not password_opcional and len(password or "") < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        if password_opcional and password and len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
