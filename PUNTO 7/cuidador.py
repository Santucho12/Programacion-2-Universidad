class Cuidador:
    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mascotas = []  # Lista de mascotas asignadas

    def agregarMascota(self,mascota:"Mascota"):
        self.__mascotas.append(mascota)

    def saberMascotas(self):
        return [str(mascota) for mascota in self.__mascotas]

    def __str__(self):
        return f"Cuidador(nombre={self.__nombre}, direccion={self.__direccion}, telefono={self.__telefono})"
 