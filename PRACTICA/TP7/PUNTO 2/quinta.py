from inmueble import Inmueble
from propietario import Propietario

class Quinta(Inmueble):
    
    def __init__(self,metrosParque:int,codigo:int,domicilio:str,propietario:"Propietario",metrosCuadrados:int,estado:int):
        super().__init__(codigo,domicilio,propietario,metrosCuadrados,estado)
        
        
        if not isinstance(metrosCuadrados,int):
            raise ValueError("El número de metros cuadrados debe ser un número entero.")
        
        self.__metrosCuadrados=metrosCuadrados
        
        
        
    def obtenerMetrosParque(self)->int:
        return self.__metrosCuadrados
    
    def establecerMetrosParque(self,metros:int)->int:
        if not isinstance(metros,int):
            raise ValueError("El número de metros cuadrados debe ser un número entero.")
        self.__metrosCuadrados=metros
        
        #no especifica como se calcula la venta ni el alquiler
        
        