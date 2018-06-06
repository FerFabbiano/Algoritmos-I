import unittest
from functions import mayusculas
from functions import minusculas
from functions import sumar


class TestMayusculasMinusculas(unittest.TestCase):

    def setUp(self):
        self.texto = "Hola Mundo!"

    def tearDown(self):
        self.texto = ""

    def test_pasar_a_mayusculas(self):
        en_mayusculas = mayusculas(self.texto)
        self.assertEqual(en_mayusculas,
                         "HOLA MUNDO!",
                         "Error, devolvio {0}!".format(en_mayusculas))

    def test_pasar_a_minusculas(self):
        en_minusculas = minusculas(self.texto)
        self.assertEqual(en_minusculas,
                         "hola mundo!",
                         "Error, devolvio {0}!".format(en_minusculas))

    def test_sumar(self):
        self.assertTrue(sumar(1, 1) == 2)
        self.assertEqual(sumar(1, 1), 2)
        self.assertEqual(sumar(-1, 1), 0) #negativos


if __name__ == '__main__':
    unittest.main()