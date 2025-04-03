import json

class Libro:
    def __init__(self, titulo:str, autor:str, genero:str, año:int, isbn:int):
        if not isinstance(titulo, str):
            raise ValueError(f'Error: el título debe ser un string')
        if not isinstance(autor, str):
            raise ValueError(f'Error: el autor debe ser un string')
        if not isinstance(genero, str):
            raise ValueError(f'Error: el género debe ser un string')
        if not isinstance(año, int):
            raise ValueError(f'Error: el año debe ser un entero')
        if not isinstance(isbn, int):
            raise ValueError(f'Error: el ISBN debe ser un entero')
        
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__año = año
        self.__isbn = isbn
    
    @classmethod
    def from_dicc(cls, data: dict):
        if not isinstance(data, dict):
            raise ValueError(f'Error: el argumento debe ser un diccionario')
        return cls(
            data['titulo'],
            data['autor'],
            data['genero'],
            data['año'],  
            data['isbn']
        )
    
    def to_dicc(self):
        return {
            'titulo': self.__titulo,
            'autor': self.__autor,
            'genero': self.__genero,
            'año': self.__año,
            'isbn': self.__isbn
        }
    


