from propietario import Propietario
class Inmueble:
    
    def __init__(self,codigo:int,domicilio:str,propietario:"Propietario",metrosCuadrados:int,estado:int):
        if not isinstance(codigo,int):
            raise ValueError("El código del inmueble debe ser un número entero.")
        if not isinstance(domicilio, str):
            raise ValueError("El domicilio del inmueble debe ser una cadena.")
        if not isinstance(propietario, Propietario):
            raise ValueError("El propietario del inmueble debe ser una instancia de la clase Propietario.")
        if not isinstance(metrosCuadrados, int):
            raise ValueError("Los metros cuadrados del inmueble debe ser un número entero.")
        if not isinstance(estado, int):
            raise ValueError("El estado del inmueble debe ser un número entero ")
        
        self._codigo=codigo
        self._domicilio=domicilio
        self._propietario=propietario
        self._metrosCuadrados=metrosCuadrados
        self._estado=estado
        
        
        
    def obtenerCodigo(self) -> int:
        return self._codigo

    def obtenerDomicilio(self) -> str:
        return self._domicilio

    def obtenerPropietario(self) -> "Propietario":
        return self._propietario

    def obtenerMetrosCuadrados(self) -> int:
        return self._metrosCuadrados

    def obtenerEstado(self) -> int:
        return self._estado
    
    
    
    
    def establecerCodigo(self, codigo: int):
        if not isinstance(codigo, int):
            raise ValueError("El código del inmueble debe ser un número entero.")
        self._codigo = codigo

    def establecerDomicilio(self, domicilio: str):
        if not isinstance(domicilio, str):
            raise ValueError("El domicilio del inmueble debe ser una cadena.")
        self._domicilio = domicilio

    def establecerPropietario(self, propietario: "Propietario"):
        if not isinstance(propietario, Propietario):
            raise ValueError("El propietario del inmueble debe ser una instancia de la clase Propietario.")
        if self._propietario is not None:
            self._propietario = propietario
        else:
            print("el inmueble ya tiene propietario")
            
    def establecerMetrosCuadrados(self, metrosCuadrados: int):
        if not isinstance(metrosCuadrados, int):
            raise ValueError("Los metros cuadrados del inmueble debe ser un número entero.")
        self._metrosCuadrados = metrosCuadrados

    def establecerEstado(self, estado: int):
        if not isinstance(estado, int):
            raise ValueError("El estado del inmueble debe ser un número entero.")
        self._estado = estado
        
        #no se como calcular el precio de venta ni el alquiler
        
        
        
        