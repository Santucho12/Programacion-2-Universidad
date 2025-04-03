from empleado import Empleado

class Administrativo(Empleado):
    def __init__(self, nombre: str, apellido: str, dni: str, legajo: int, posicion: str):
        super().__init__(nombre, apellido, dni, legajo)
        
        if not isinstance(posicion, str):
            raise ValueError("La posición debe ser una cadena de caracteres.")
        
        self.__posicion = posicion
    
    def __str__(self):
        return f"{super().__str__()}, Posición: {self.__posicion}"
