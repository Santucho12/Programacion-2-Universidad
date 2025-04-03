import json

class Tester:
    def cargarMostrar(self, libros_json):
            with open(libros_json, "r" ,encoding="utf-8") as archivo:
                data = json.load(archivo)
                for libro in data:
                    print(libro)
                    
    def buscarXaño(self, libros_json):
        # Convertir la entrada del año a entero
        año = int(input("Ingrese el año: "))
        print(f"Libros encontrados por año {año}:")
        with open(libros_json, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            # Buscar libros que coincidan con el año
            for libro in data:
                if 'año' in libro and libro['año'] == año:
                    print(libro)
                
if __name__ == "__main__":
    libros_json = "c:/Users/AMDRYZEN7/Desktop/Programacion 2/PRACTICA/tp8/punto 1/libros.json"
    Tester().cargarMostrar(libros_json)
    Tester().buscarXaño(libros_json)