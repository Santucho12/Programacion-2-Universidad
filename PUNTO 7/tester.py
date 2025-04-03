# main.py
from mascota import Mascota
from cuidador import Cuidador

if __name__ == "__main__":
    # Crear cuidadores
    cuidador1 = Cuidador("Juan Perez", "Calle Falsa 123", "123456789")
    cuidador2 = Cuidador("Maria Lopez", "Avenida Siempre Viva 742", "987654321")
    
    # Crear mascotas
    mascota1 = Mascota("Rex", "Perro", 5, "Perro guardián y cariñoso.")
    mascota2 = Mascota("Miau", "Gato", 3, "Gato juguetón y curioso.")
    
    # Asignar mascotas a cuidadores
    mascota1.asignarCuidador(cuidador1)
    mascota2.asignarCuidador(cuidador2)
    
    # Mostrar información
    print(cuidador1)
    print(f"Mascotas de {cuidador1.saberMascotas()}")
    
    print(cuidador2)
    print(f"Mascotas de {cuidador2.saberMascotas()}")
