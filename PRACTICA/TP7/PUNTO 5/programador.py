from empleado import Empleado

class Programador(Empleado):
    def __init__(self,nombre:str,apellido:str,dni:str,legajo:int,area:str):   
        super().__init__(nombre,apellido,dni,legajo)    
        
        if not isinstance(area,str):
            raise ValueError("area debe ser un string.")
        
        self.__area = area