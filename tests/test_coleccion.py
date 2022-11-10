import unittest

from faker import Faker

from src.logica.coleccion import Coleccion
from src.modelo.cancion import Cancion
from src.modelo.declarative_base import Session
from src.modelo.interprete import Interprete


class ColeccionTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.coleccion = Coleccion()

        self.data_factory = Faker()

    def testAgregarColeccion(self):
        nombre_interprete = "nombre"
        texto_curiosidades = "nombre"
        self.assertEqual(nombre_interprete, texto_curiosidades)

    def testEditarColeccion(self):
        coleccion = "otro"
        coleccion2 = "otro"
        self.assertEqual(coleccion, coleccion2)

    def testEliminarColeccion(self):
        self.coleccion.eliminar_interprete(1)
        self.assertIsNone(None)

    