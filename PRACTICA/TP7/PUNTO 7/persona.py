from abc import ABC,abstractmethod
from datetime import datetime

class Persona(ABC):
    def __init__(self,dni:int,nombre:str,apellido:str,fecha:datetime):
        if not isinstance(dni,int):
            raise ValueError("El DNI debe ser un número entero.")
        if not isinstance(nombre, str) or not nombre.isalpha():
            raise ValueError("El nombre debe ser una cadena de caracteres alfabéticos.")
        if not isinstance(apellido, str) or not apellido.isalpha():
            raise ValueError("El apellido debe ser una cadena de caracteres alfabéticos.")
        if not isinstance(fecha, datetime):
            raise ValueError("La fecha de nacimiento debe ser una fecha.")
        
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._fecha = fecha
        
    
    def __str__(self):
        return f"el nombre es {self._nombre} {self._apellido} y su dni es {self._dni}"