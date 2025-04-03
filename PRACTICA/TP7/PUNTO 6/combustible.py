class Combustible:
    
    def __init__(self,tipo:str):
        
        if not isinstance(tipo,str):
            raise ValueError("El tipo de combustible debe ser una cadena.")
        
        self.__tipo = tipo
        
    def __str__(self):
        
        return f"Tipo de combustible: {self.__tipo}"