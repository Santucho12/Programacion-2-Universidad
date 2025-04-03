class Empleado:
    def __init__(self, nombre: str, apellido: str, dni: str, legajo: int):
        if not isinstance(nombre, str):
            raise ValueError("Nombre debe ser una cadena")
        if not isinstance(apellido, str):
            raise ValueError("Apellido debe ser una cadena")
        if not isinstance(dni, str):
            raise ValueError("DNI debe ser una cadena")
        if not isinstance(legajo, int):
            raise ValueError("Legajo debe ser un entero")
        
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._legajo = legajo
    
    def __str__(self):
        return f"Empleado: {self._nombre} {self._apellido}, DNI: {self._dni}, Legajo: {self._legajo}"
