from datetime import date as Fecha
from datetime import timedelta 
from datetime import date
from Socio import Socio
from libro import Libro
class Prestamo:
    def __init__(self,libro:Libro,fechaPrestamo:Fecha,cantDias:int,socio:Socio):
        
        if not isinstance(libro,Libro):
            raise ValueError("el supuesto libro debe ser un libro")
        self.__libro = libro
        
        if not isinstance(fechaPrestamo, Fecha):
            raise ValueError("la fecha del prestamo debe ser una fecha")
        self.__fechaPrestamo = fechaPrestamo
        
        if not isinstance(cantDias,int) or cantDias <=0:
            raise ValueError("la cantidad de dias debe ser un numero entero y positivo")
        self.__cantDias = cantDias
        
        if not isinstance(socio, Socio):
            raise ValueError("el supuesto socio debe ser un socio")
        self.__socio = socio
        
        self.__fechaDevolucion=None
        
    def establecerFechaDevolucion(self,fechadevuelto:Fecha):
        if not isinstance(fechadevuelto, Fecha):
            raise ValueError("la fecha de devolucion debe ser una fecha")
        self.__fechaDevolucion = self.__fechaPrestamo + timedelta(days=self.__cantDias)
        if self.__fechaDevolucion<fechadevuelto: 
            self.__socio.establecerFechaPenanalizacion(self.__fechadevuelto)
            
        
    
    
    def obtenerLibro(self)->Libro:
        return self.__Libro
    
    
    def obtenerFechaPrestramo(self)->Fecha:
        return self.__fechaPrestamo
    
    def obtenerFechaDevolucion(self)->Fecha:
        return self.__fechadevuelto
    
    def estaAtrasado(self)->bool:
        return self.__fechadevuelto < date.today()
    
    def penalizacion(self)->Fecha:
        if self.__fechaDevolucion is not None:
            
            if self.__fechadevuelto>=date.today()+timedelta(days=21):
                fechaPenalizacion=date.today()+timedelta(days=10)
                
            elif self.__fechadevuelto>=date.today()+timedelta(days=20):
                fechaPenalizacion=date.today()+timedelta(days=5)
                
            elif self.__fechadevuelto>=date.today()+timedelta(days=7):
                fechaPenalizacion=date.today()+timedelta(days=3)
            
            if self.__libro.obtenerCategoria()=="A":
                fechaPenalizacion=fechaPenalizacion+timedelta(days=fechaPenalizacion)
            
        return fechaPenalizacion
            
            
    
    def __str__(self)->str:
        return f"el libro es :{self.__libro}, el socio al que le pertenece es {self.__socio}, la fecha de prestamo es {self.__fechaPrestamo}, los dias que tiene para devolverlo son {self.__cantDias}, por lo tanto la fecha para devolverlo es : {self.__fechaDevolucion}"
    
        