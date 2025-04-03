from datetime import datetime as Fecha
from participante import Participante
from organizador import Organizador
from evento import Evento
class Tester:
    def probarTest(self):
        print("Probando el test")
        organizador = Organizador("Ana Gómez", "ana@example.com", "Planificación de eventos")
        print(organizador)

        evento1 = Evento("Conferencia de Tecnología", Fecha(2024, 10, 20), "Una conferencia sobre tecnología innovadora.")
        evento2 = Evento("Taller de Programación", Fecha(2024, 11, 15), "Taller práctico de programación.")
        print(evento1)
        print(evento2)

        organizador.agregarEvento(evento1)
        organizador.agregarEvento(evento2)

        print("Eventos a cargo del organizador:")
        for evento in organizador.obtenerEventos():
            print(evento.obtenerNombre())

        participante1 = Participante("Juan Pérez", "juan@example.com", "123456789")
        participante2 = Participante("María López", "maria@example.com", "987654321")
        print(participante1)
        print(participante2)

        participante1.agregarEvento(evento1)
        participante2.agregarEvento(evento2)

        print("Eventos registrados por Juan Pérez:")
        for evento in participante1.obtenerEventos():
            print(evento.obtenerNombre())

        print("Eventos registrados por María López:")
        for evento in participante2.obtenerEventos():
            print(evento.obtenerNombre())

        print(f"Participantes en el evento '{evento1.obtenerNombre()}':")
        for participante in evento1.obtenerParticipantes():
            print(participante)

        print(f"Participantes en el evento '{evento2.obtenerNombre()}':")
        for participante in evento2.obtenerParticipantes():
            print(participante)

        print(organizador)
        print(participante1)
        print(participante2)

