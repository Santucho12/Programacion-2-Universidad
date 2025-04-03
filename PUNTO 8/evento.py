from datetime import datetime as Fecha
class Evento:
    
    def __init__(self,nombre:str,fecha:Fecha,descripcion:str):
        if not isinstance(nombre,str):
            raise ValueError("Nombre del evento debe ser una cadena.")
        if not isinstance(fecha, Fecha):
            raise ValueError("La fecha debe ser una instancia de datetime")
        if not isinstance(descripcion,str): 
            raise ValueError("La descripción del evento debe ser una cadena.")
        self.__nombre = nombre
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__participantes = []
        self.__organizador=None
        
        
    def obtenerNombre(self) -> str:
        return self.__nombre

    def obtenerFecha(self) -> Fecha:
        return self.__fecha

    def obtenerDescripcion(self) -> str:
        return self.__descripcion
    
    
    
    def establecerNombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre del evento debe ser una cadena.")
        self.__nombre = nombre

    def establecerFecha(self, fecha: Fecha):
        if not isinstance(fecha, Fecha):
            raise ValueError("La fecha debe ser una instancia de datetime.")
        self.__fecha = fecha

    def establecerDescripcion(self, descripcion: str):
        if not isinstance(descripcion, str):
            raise ValueError("La descripción del evento debe ser una cadena.")
        self.__descripcion = descripcion
        
        
        
    
    
    
    def obtenerOrganizador(self):
        return self.__organizador

    def establecerOrganizador(self, organizador: "Organizador"):
        if not isinstance(organizador, Organizador):
            raise ValueError("El organizador debe ser una instancia de la clase Organizador.")
        self.__organizador = organizador

    
    
    
    def agregarParticipante(self, participante: "Participante"):
        if not isinstance(participante, Participante):
            raise ValueError("El participante debe ser una instancia de la clase Participante.")
        self.__participantes.append(participante)

    def obtenerParticipantes(self):
        return self.__participantes
    
    
    
    def __repr__(self):
        organizador_repr = repr(self.__organizador) if self.__organizador else "None"
        participantes_repr = [repr(participante) for participante in self.__participantes]
        return (f"Evento(nombre={self.__nombre!r}, fecha={self.__fecha!r}, "
                f"descripcion={self.__descripcion!r}, organizador={organizador_repr}, "
                f"participantes={participantes_repr})")

