from abc import ABC, abstractmethod


class UsuarioRepository(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, usuario_id):
        pass

    @abstractmethod
    def obtener_por_username(self, username):
        pass

    @abstractmethod
    def obtener_por_email(self, email):
        pass

    @abstractmethod
    def crear(self, usuario):
        pass

    @abstractmethod
    def actualizar(self, usuario):
        pass

    @abstractmethod
    def eliminar(self, usuario):
        pass
