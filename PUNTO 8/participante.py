class Participante:
    
    def __init__(self,nombre:str,gmail:str,telefono:int):
        if not isinstance(nombre,str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        if not isinstance(gmail, str):
            raise ValueError("El correo electrónico debe ser una cadena de caracteres.")
        if not isinstance(telefono, int):
            raise ValueError("El número de teléfono debe ser un entero.")
        self.__nombre = nombre
        self.__gmail = gmail
        self.__telefono = telefono
        self.__eventos = []
        
    def obtenerNombre(self) -> str:
        return self.__nombre

    def obtenerEmail(self) -> str:
        return self.__email

    def obtenerTelefono(self) -> str:
        return self.__telefono
    
    
    def establecerNombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena.")
        self.__nombre = nombre

    def establecerEmail(self, email: str):
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("La dirección de correo electrónico no es válida.")
        self.__email = email

    def establecerTelefono(self, telefono: str):
        if not isinstance(telefono, str):
            raise ValueError("El número de teléfono debe ser una cadena.")
        self.__telefono = telefono

   
    def agregarEvento(self, evento: "Evento"):
        if not isinstance(self,evento):
            raise ValueError("El parámetro debe ser un evento.")
        if evento not in self.__eventos:
            self.__eventos.append(evento)
            evento.agregarParticipante(self)
   
   
    def obtenerListaEventos(self):
        return self.__eventos
   
   
   
   
   
   
   
   
   
        
    def __str__(self):
        return f"Participante: {self.__nombre}, Email: {self.__email}, Teléfono: {self.__telefono}"

    def __repr__(self):
        return (f"Participante(nombre={self.__nombre!r}, email={self.__email!r}, "
                f"telefono={self.__telefono!r}, eventos={self.__eventos!r})")