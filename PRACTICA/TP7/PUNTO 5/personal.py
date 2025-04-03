from empleado import Empleado

class Personal(Empleado):
    def __init__(self,nombre:str,apellido:str,dni:str,legajo:int,proyectos:int):   
        super().__init__(nombre,apellido,dni,legajo)    
        
        if not isinstance(proyectos,int):
            raise ValueError("Proyectos debe ser un entero.")
        
        self.__proyectos = proyectos
        
    def __str__(self):
       return f"El nombre es: {self._nombre}, Apellido: {self._apellido}, DNI: {self._dni}, Legajo: {self._legajo}, Proyectos: {self.__proyectos}"
