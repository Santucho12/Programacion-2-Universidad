from administrativo import Administrativo
from personal import Personal
from programador import Programador

class Tester:
    def run(self):
        administrativo1 = Administrativo("Santiago", "Segal", "43263852", 1, "mano de obra")
        personal1 = Personal("bautista", "tordini", "43263852", 2,4)
        print(administrativo1) 
        print()
        print(personal1)
        programador1 = Programador("abner", "grhgurich", "43263852", 3,"limpieza")
        print()
        print(programador1)



if __name__ == "__main__":
    Tester().run()
    