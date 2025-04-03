from vehiculo import Vehiculo
from combustible import Combustible

class Motos(Vehiculo):
    def __init__(self, marca: str, modelo: str, patente: str, color: str, año: int, precio: float, kilometraje: int, combustible: Combustible, espejos: int):
        super().__init__(marca, modelo, patente, color, año, precio, kilometraje, combustible)

        if not isinstance(espejos, int):
            raise ValueError("La cantidad de espejos debe ser un entero.")
        
        self.__espejos = espejos

    def __str__(self):
        return f"la moto es : Marca: {self._marca}, Modelo: {self._modelo}, Patente: {self._patente}, Color: {self._color}, Año: {self._año}, Precio: ${self._precio}, Kilometraje: {self._kilometraje} km, Combustible: {self._combustible}, espejos: {self.__espejos}"
