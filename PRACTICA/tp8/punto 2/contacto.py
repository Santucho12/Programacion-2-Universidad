class Contacto:
    def __init__(self,nombre:str,apellido:str,telefono:int):
        if not isinstance(nombre,str):
            raise ValueError(f'Nombre debe ser un string')
        if not isinstance(apellido,str):
            raise ValueError(f'Apellido debe ser un string')
        if not isinstance(telefono,int):
            raise ValueError(f'Telefono debe ser un numero')
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        
    
    def to_dicc(self):
        return {
            'nombre':self.nombre,
            'apellido':self.apellido,
            'telefono':self.telefono
        }   
        
    @classmethod
    def from_dicc(cls,dicc:dict):
        return cls(dicc['nombre'],dicc['apellido'],dicc['telefono'])
    