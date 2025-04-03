from evento import Evento
class Organizador:
    def __init__(self, nombre: str, email: str, especialidad: str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena.")
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("La dirección de correo electrónico no es válida.")
        if not isinstance(especialidad, str):
            raise ValueError("La especialidad debe ser una cadena.")

        self.__nombre = nombre
        self.__email = email
        self.__especialidad = especialidad
        self.__eventos = []  # Lista de eventos a cargo

    # Métodos para obtener atributos
    def obtenerNombre(self) -> str:
        return self.__nombre

    def obtenerEmail(self) -> str:
        return self.__email

    def obtenerEspecialidad(self) -> str:
        return self.__especialidad

    def obtenerEventos(self) -> list:
        return self.__eventos

    # Método para agregar un evento
    def agregarEvento(self, evento: "Evento"):
        if not isinstance(evento, Evento):
            raise ValueError("El evento debe ser una instancia de la clase Evento.")
        if evento not in self.__eventos:
            self.__eventos.append(evento)

    # Método __str__ para representación legible
    def __str__(self):
        return f"Organizador: {self.__nombre}, Email: {self.__email}, Especialidad: {self.__especialidad}"

    # Método __repr__ para representación técnica
    def __repr__(self):
        return (f"Organizador(nombre={self.__nombre!r}, email={self.__email!r}, "
                f"especialidad={self.__especialidad!r}, eventos={self.__eventos!r})")
