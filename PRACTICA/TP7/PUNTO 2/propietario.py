class Propietario:
    
    def __init__(self,nombre:str,edad:int):
        if not isinstance(nombre,str): raise ValueError
        if not isinstance(edad, int) or edad < 0: raise ValueError
        self.__nombre = nombre
        self.__edad = edad
        
    def obtenerEdad(self):
        return self.__edad
    
    def obtenerNombre(self):
        return self.__nombre
    
    def establecerEdad(self, nuevaEdad:int):
        if not isinstance(nuevaEdad, int) or nuevaEdad < 0: raise ValueError
        self.__edad = nuevaEdad
        
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre, str): raise ValueError
        self.__nombre = nombre
        
   
        
        