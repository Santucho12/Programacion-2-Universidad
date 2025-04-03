class Libro:
    
    def __init__(self,nombre:str,autor:str,editorial:str,categoria:str):
        if not isinstance(nombre,str):
            raise ValueError("El nombre del libro debe ser texto ")
        self.nombre = nombre
        if not isinstance(autor,str):
            raise ValueError("El nombre del autor debe ser texto ")
        self.autor = autor
        if not isinstance(editorial,str):
            raise ValueError("El nombre de la editorial debe ser texto ")
        self.editorial = editorial

        if categoria not in ["A","B","C"]:
            raise ValueError("la categoria del libro debe ser un caracter dentro de las opciones")
        self.categoria = categoria
        
        
    def obtenerNombre(self)->str:
        return self.nombre
    
    def obtenerAutor(self)->str:
        return self.autor
    
    def obtenerEditorial(self)->str:
        return self.editorial
    
    def obtenerCategoria(self)->str:
        return self.categoria
    
    def __str__(self)->str:
        return f"Libro: {self.nombre}, Autor: {self.autor}, Editorial: {self.editorial}, Categoria: {self.categoria}"