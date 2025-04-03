from persona import Persona
from datetime import datetime
class EmpleadoComision(Persona):
    
    def __init__(self,dni:int,nombre:str,apellido:str,fecha:datetime,salariomin:int,cantidadclientes:int,montoporcliente:int):
        super().__init__(dni, nombre, apellido, fecha)
        
        if not isinstance(salariomin,int):
            raise ValueError('El salario mínimo debe ser un número entero.')
        if not isinstance(cantidadclientes,int):
            raise ValueError('El error se debe a que no es un numero.')
        if not isinstance(montoporcliente,int):
            raise ValueError('El monto por cliente debe ser un número entero.')
        
        self.__salariomin = salariomin
        self.__cantidadclientes = cantidadclientes
        self.__montoporcliente = montoporcliente
        
    def calculoSueldo(self):
            if self.__salariomin >= self.__cantidadclientes*self.__montoporcliente:
                print("vas a cobrar el sueldo minimo")
                return self.__salariomin
            else:
                print("cobras con comision perro")
                return self.__cantidadclientes*self.__montoporcliente
            
            
    def __str__(self):
            return f"el nombre es ¨{self._nombre} {self._apellido} y su dni es {self._dni} es un empleado a comision y su sueldo es {self.calculoSueldo()}"
