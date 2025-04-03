from combustible import Combustible
from vehiculo import Vehiculo
from autos import Autos
from motos import Motos

class tester:
    def run(self):
        
        combustible1=Combustible("nafta")
        vehiculo1=Vehiculo("peugeot","208","2k23","amarillo",2022,10500.5,1000000000000,combustible1)
        auto1=Autos("peugeot","408","2k25","rojo",2022,10500.5,1000000000000,combustible1,5)
        moto1=Motos("racer","408","2k25","rojo",2022,10500.5,1000000000000,combustible1,2)
        
        
        print(vehiculo1)
        print(auto1)
        print(moto1)
        
        
if __name__ == "__main__":
    tester().run()
    #hola probandosakksa kfnaflnm