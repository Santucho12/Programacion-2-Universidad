# Una concesionaria de automóviles vende una gran variedad de vehículos. Cada
# vehículo tiene una marca, modelo, patente, color, año de fabricación, precio y un
# determinado kilometraje. Además, se registra el tipo de combustible que utiliza
# (nafta, diésel o eléctrico). Los autos, además de las características generales de un
# vehículo, tienen una cantidad específica de puertas y algunos cuentan con aire
# acondicionado. Por otro lado, las motos tienen un ancho de manubrio y una
# cilindrada particular.
from combustible import Combustible
class Vehiculo:
    
    def __init__(self,marca:str,modelo:str,patente:str,color:str,año:int,precio:float,kilometraje:int,combustible:Combustible):
        if not isinstance(marca,str):
            raise ValueError("Marca debe ser una cadena.")
        if not isinstance(modelo,str):
            raise ValueError("Modelo debe ser una cadena.")
        if not isinstance(patente,str):
            raise ValueError("Patente debe ser una cadena.")
        if not isinstance(color,str):
            raise ValueError("Color debe ser una cadena.")
        if not isinstance(año,int) or año < 1900 or año > 2022:
            raise ValueError("Año de fabricación debe ser un entero entre 1900 y 2022.")
        if not isinstance(precio, float):
            raise ValueError("Precio debe ser un número decimal.")
        if not isinstance(kilometraje, int):
            raise ValueError("Kilometraje debe ser un entero.")
        if not isinstance(combustible, Combustible):
            raise ValueError("Combustible debe ser un objeto de la clase Combustible.")
        
        self._marca = marca
        self._modelo = modelo
        self._patente = patente
        self._color = color
        self._año = año
        self._precio = precio
        self._kilometraje = kilometraje
        self._combustible = combustible
        
        
    def __str__(self):
        return f"{self._marca} {self._modelo} - Patente: {self._patente}, Color: {self._color}, Año de fabricación: {self._año}, Precio: ${self._precio}, Kilometraje: {self._kilometraje} km, Combustible: {self._combustible}"