from quinta import Quinta
from propietario import Propietario
from inmueble import Inmueble
from depto import Depto

class Tester:
    @staticmethod
    def testPropiedades():
        # Crear un propietario
        propietario1 = Propietario("Juan Pérez", 30)
        
        # Crear una Quinta
        quinta = Quinta(200, 1, "Calle Falsa 123", propietario1, 500, 1)
        print(f"Quinta - Código: {quinta.obtenerCodigo()}, Domicilio: {quinta.obtenerDomicilio()}, Propietario: {quinta.obtenerPropietario().obtenerNombre()}, Metros Cuadrados: {quinta.obtenerMetrosCuadrados()}")

        # Crear un Depto
        depto = Depto(1500, True, 2, "Avenida Siempre Viva 742", propietario1, 75, 1)
        print(f"Depto - Código: {depto.obtenerCodigo()}, Domicilio: {depto.obtenerDomicilio()}, Propietario: {depto.obtenerPropietario().obtenerNombre()}, Gastos Comunes: {depto.obtenerGastosComunes()}, Cochera: {depto.obtenerCochera()}")

        # Modificar y obtener atributos
        depto.establecerGastosComunes(1600)
        print(f"Gastos Comunes Actualizados: {depto.obtenerGastosComunes()}")

        # Cambiar el propietario de la Quinta
        propietario2 = Propietario("Ana Gómez", 28)
        quinta.establecerPropietario(propietario2)
        print(f"Nuevo Propietario de la Quinta: {quinta.obtenerPropietario().obtenerNombre()}")

if __name__ == '__main__':
    Tester().testPropiedades()