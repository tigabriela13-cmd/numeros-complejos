import unittest
import math
from complejos import operaciones as op

class TestOperacionesComplejos(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(op.suma((3, 2), (1, -1)), (4, 1))
        self.assertEqual(op.suma((0, 0), (2, 5)), (2, 5))

    def test_resta(self):
        self.assertEqual(op.resta((3, 2), (1, 1)), (2, 1))
        self.assertEqual(op.resta((0, 0), (2, 5)), (-2, -5))

    def test_producto(self):
        self.assertEqual(op.producto((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(op.producto((0, 1), (0, 1)), (-1, 0))

    def test_division(self):
      self.assertEqual(op.division((1, 2), (1, -1)), (1.5, 0.5))
      with self.assertRaises(ZeroDivisionError):
        op.division((1, 2), (0, 0))


    def test_modulo(self):
        self.assertEqual(op.modulo((3, 4)), 5)
        self.assertAlmostEqual(op.modulo((1, 1)), math.sqrt(2))

    def test_conjugado(self):
        self.assertEqual(op.conjugado((3, 4)), (3, -4))
        self.assertEqual(op.conjugado((-2, -5)), (-2, 5))

    def test_cartesiano_a_polar(self):
        r, theta = op.cartesiano_a_polar((1, 1))
        self.assertAlmostEqual(r, math.sqrt(2))
        self.assertAlmostEqual(theta, math.pi/4)

    def test_polar_a_cartesiano(self):
        a, b = op.polar_a_cartesiano((2, math.pi/2))
        self.assertAlmostEqual(a, 0, places=5)
        self.assertAlmostEqual(b, 2, places=5)

    def test_fase(self):
        self.assertEqual(round(op.fase((1, 1)), 2), round(math.pi/4, 2))
        self.assertEqual(round(op.fase((0, -1)), 2), round(-math.pi/2, 2))

if __name__ == "__main__":
    unittest.main()
