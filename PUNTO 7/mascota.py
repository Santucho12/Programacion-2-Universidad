class Mascota:
    
    def __init__(self,nombre:str,especie:str,edad:int,descripcion:str):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__descripcion = descripcion
        self.__cuidador=None
        
    
    def esatblecerNombre(self,nombre:str):
        if not isinstance(nombre,str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        self.__nombre = nombre
        
    def establecerEspecie(self,especie:str):
        if not isinstance(especie,str):
            raise ValueError("El nombre de la especie debe ser una cadena de caracteres.")
        self.__especie = especie
        
    def establecerEdad(self,edad:int):
        if not isinstance(edad,int):
            raise ValueError("la edad debe ser un numero")
        self.__edad = edad
        
    def establecerDescripcion(self,descripcion:str):
        if not isinstance(descripcion,str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        self.__descripcion = descripcion
        
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEspecie(self)->str:
        return self.__especie
    
    def obtenerEdad(self)->int:
        return self.__edad
    
    def obtenerDescripcion(self)->str:
        return self.__descripcion
    
    def asignarCuidador(self,cuidador:"Cuidador"):
        self.__cuidador = cuidador
        cuidador.agregarMascota(self)
    
    def conocerCuidador(self):
        return self.__cuidador
    
    def __str__(self):
        return f"nombre={self.__nombre}, especie={self.__especie}, edad={self.__edad}, descripcion={self.__descripcion}"
