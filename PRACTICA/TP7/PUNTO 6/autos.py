from vehiculo import Vehiculo
from combustible import Combustible

class Autos(Vehiculo):
    def __init__(self, marca: str, modelo: str, patente: str, color: str, año: int, precio: float, kilometraje: int, combustible: Combustible, puertas: int):
        super().__init__(marca, modelo, patente, color, año, precio, kilometraje, combustible)

        if not isinstance(puertas, int):
            raise ValueError("La cantidad de puertas debe ser un entero.")
        
        self.__puertas = puertas

    def __str__(self):
        return f"el Auto es : Marca: {self._marca}, Modelo: {self._modelo}, Patente: {self._patente}, Color: {self._color}, Año: {self._año}, Precio: ${self._precio}, Kilometraje: {self._kilometraje} km, Combustible: {self._combustible}, Puertas: {self.__puertas}"
