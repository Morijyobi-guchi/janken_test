import unittest
from source.add import add

# テストクラス
class TestAddModule(unittest.TestCase):

    def test_add_integers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_floats(self):
        result = add(2.5, 3.5)
        self.assertAlmostEqual(result, 6.0, places=2)

    def test_add_strings(self):
        result = add("Hello, ", "world!")
        self.assertEqual(result, "Hello, world!")