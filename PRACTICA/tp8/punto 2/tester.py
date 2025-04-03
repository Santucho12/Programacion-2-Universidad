import json
from contacto import Contacto

class Tester:
    def run(self):
        contacto1=Contacto('Juan','Perez',123456)
        contacto2=Contacto('Maria','Gomez',654321)
        contacto3=Contacto('Carlos','Lopez',987654)
        contacto4=Contacto('Ana','Martinez',456789)
        listaContactos=[contacto1,contacto2,contacto3,contacto4]
        
        with open("contactos.json","w") as file:
            contactos_dict = []
            for contacto in listaContactos:
                contactos_dict.append(contacto.to_dicc())
            json.dump(contactos_dict, file)
            
        with open("contactos.json", "r") as file:
            contactos_reconstruidos = []
            contactos_dict = json.load(file)
            for contacto in contactos_dict:
                contactos_reconstruidos.append(Contacto.from_dicc(contacto))
                
        letra = input("Ingrese una letra para buscar contactos por apellido: ")
        contactos_filtrados = []
        for contacto in contactos_reconstruidos:
            if contacto.apellido.startswith(letra):
                contactos_filtrados.append(contacto)
            
        print("Contactos encontrados:")
        for contacto in contactos_filtrados:
            print(f"{contacto.nombre} {contacto.apellido} - {contacto.telefono}")
        
     
        

if __name__ == '__main__':
    tester = Tester()
    tester.run()
    