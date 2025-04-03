from persona import Persona
from datetime import datetime

class EmpleadoFijo(Persona):
    
    def __init__(self,dni:int,nombre:str,apellido:str,fecha:datetime,sueldo_basico:float):
        super().__init__(dni, nombre, apellido, fecha)
        
        if not isinstance(sueldo_basico,float):
            raise ValueError("sueldo_basico debe ser un numero")
        
        self.__sueldo_basico = sueldo_basico
    
    def calcularAntiguedad(self):
        return datetime.now().year-self._fecha.year
        
    def calcularSalario(self):
        if self.calcularAntiguedad()<2:
            return self.__sueldo_basico
        elif self.calcularAntiguedad()>=2 and self.calcularAntiguedad()<5:
            return self.__sueldo_basico*1.05
        else:
            return self.__sueldo_basico*1.10



    def __str__(self):
        return f"el nombre es {self._nombre} {self._apellido} y su dni es {self._dni} es un empleado fijo y su sueldo es {self.calcularSalario()}"
