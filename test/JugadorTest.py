import unittest
from clases.mundo.Jugador import Jugador
class ClienteTest(unittest.TestCase):
    jugador1=Jugador(1,'Byron Trejo')
    jugador2=Jugador(2,'Daniela Coral')
    def testCliente(self):
        self.assertEqual('Byron Trejo',self.jugador1.darNombre(),'El nombre del jugador esta equivocado')
        self.assertEqual('2', self.jugador2.darId(), 'El id del jugador esta equivocado')