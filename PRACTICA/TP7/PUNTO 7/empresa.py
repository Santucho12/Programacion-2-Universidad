from empleadoFijo import EmpleadoFijo
from empleadoComision import EmpleadoComision

class Empresa:
    
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado._nombre} {empleado._apellido} agregado.")

    def eliminar_empleado(self, dni):
        for empleado in self.empleados:
            if empleado._dni == dni:
                self.empleados.remove(empleado)
                print(f"Empleado {empleado._nombre} {empleado._apellido} eliminado.")
                return
        print("Empleado no encontrado.")

    def consultar_salarios(self):
        for empleado in self.empleados:
            print(empleado)

    def empleado_con_mas_clientes(self):
        max_clientes = -1
        empleado_max = None
        for empleado in self.empleados:
            if isinstance(empleado, EmpleadoComision):
                if empleado.__cantidadclientes > max_clientes:
                    max_clientes = empleado.__cantidadclientes
                    empleado_max = empleado
        
        if empleado_max:
            print(f"Empleado a comisión con más clientes: {empleado_max._nombre} {empleado_max._apellido} con {max_clientes} clientes.")
        else:
            print("No hay empleados a comisión registrados.")
