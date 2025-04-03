from empleadoFijo import EmpleadoFijo
from empleadoComision import EmpleadoComision
from datetime import datetime
from empresa import Empresa

class Tester:
    def run(self):
        
        empleado_fijo1=EmpleadoFijo(43263852,"santiago","segal",datetime(2023,1,1),100.000)
        empleado_fijo2=EmpleadoFijo(43263852,"santiago","segal",datetime(2022,1,1),100.000)
        empleado_fijo3=EmpleadoFijo(43263852,"santiago","segal",datetime(2010,1,1),100.000)
        print(empleado_fijo1)
        print(empleado_fijo2)
        print(empleado_fijo3)
        print()
        print()
        print()
        empleadocomision1=EmpleadoComision(43263852,"santiago","segal",datetime(2023,1,1),100,10,10)
        empleadocomision2=EmpleadoComision(43263852,"santiago","segal",datetime(2023,1,1),100,20,10)
        empleadocomision3=EmpleadoComision(43263852,"santiago","segal",datetime(2023,1,1),100,20,15)
        print(empleadocomision1)
        print(empleadocomision2)
        print(empleadocomision3)
        print()
        print()
        empresa=Empresa
        empresa.agregar_empleado(empleado_fijo1)
        empresa.agregar_empleado(empleado_fijo2)
        empresa.agregar_empleado(empleadocomision1)
        empresa.agregar_empleado(empleadocomision2)

        # Consultar salarios
        print("\nSalarios de los empleados:")
        empresa.consultar_salarios()

        # Encontrar el empleado a comisión con más clientes
        empresa.empleado_con_mas_clientes()

        # Eliminar un empleado
        print("\nEliminando empleado fijo1 (Santiago Segal)...")
        empresa.eliminar_empleado(43263852)  # Eliminar empleado_fijo1
        print("\nSalarios después de eliminar a Santiago Segal:")
        empresa.consultar_salarios()


if __name__ == "__main__":
    Tester().run()