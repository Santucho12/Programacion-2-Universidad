from datetime import date as Fecha
class Socio:
    
    def __init__(self,nombre:str,fechaNacimiento:Fecha,fechaPenalizacion=None):
        if not isinstance(nombre,str):
            raise ValueError("el nombre debe ser un string")
        self.__nombre=nombre
            
        if not isinstance(fechaNacimiento,Fecha):
            raise ValueError("fecha de nacimiento debe ser de tipo fecha")        
        self.__fechaNacimiento=fechaNacimiento  
    
    
    
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str):
            raise ValueError("el nombre debe ser un string")
        self.__nombre=nombre
        
    
    def establecerFechaNacimiento(self,fecha:Fecha):
        if not isinstance(fecha,Fecha):
            raise ValueError("fecha de nacimiento debe ser de tipo fecha")        
        self.__fechaNacimiento=fecha
    
        
    def establecerFechaPenalizacion(self,fecha:Fecha):
        if not isinstance(fecha,Fecha):
            raise ValueError("fecha de penalización debe ser de tipo fecha")        
        self.__fechaPenalizacion=fecha
        
    
    
    
    
    
    def estaHabilitado(self,fecha:Fecha)->bool:
        return self.__fechaPenalizacion is None or self.__fechaPenalizacion<fecha
            
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerFechaNacimiento(self)->Fecha:
        return self.__fechaNacimiento
    
    def obtenerFechaPenalizacion(self)->Fecha:
        return self.__fechaPenalizacion
    
    def __str__(self)->str:
        return f"Nombre: {self.__nombre}, Fecha de Nacimiento: {self.__fechaNacimiento}, Fecha de Penalización: {self.__fechaPenalizacion}"