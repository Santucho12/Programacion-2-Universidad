from inmueble import Inmueble
class Depto(Inmueble):
    
    def __init__(self, gastosComunes: int, cochera: bool, codigo: int, domicilio: str, propietario: "Propietario", metrosCuadrados: int, estado: int):
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        
        if not isinstance(gastosComunes, int):
            raise ValueError("Los gastos comunes deben ser un número entero.")
        if not isinstance(cochera, bool):
            raise ValueError("La cochera debe ser un booleano.")
        
        self.__gastosComunes = gastosComunes  # Atributo privado para gastos comunes
        self.__cochera = cochera  # Atributo privado para cochera
        
    def obtenerGastosComunes(self) -> int:
        return self.__gastosComunes  # Acceder al atributo privado

    def obtenerCochera(self) -> bool:
        return self.__cochera  # Acceder al atributo privado

    def establecerGastosComunes(self, gastosComunes: int):
        if not isinstance(gastosComunes, int):
            raise ValueError("Los gastos comunes deben ser un número entero.")
        self.__gastosComunes = gastosComunes  # Actualizar el atributo privado

    def establecerCochera(self, cochera: bool):
        if not isinstance(cochera, bool):
            raise ValueError("Cochera debe ser un valor booleano.")
        self.__cochera = cochera  # Actualizar el atributo privado
