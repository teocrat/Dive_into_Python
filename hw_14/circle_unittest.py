import unittest
from circle import Circle


class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Circle(3)

    def test_len(self):
        self.assertEqual(self.c.len_circle(), 18.84955592153876)

    def test_square(self):
        self.assertEqual(self.c.square(), 28.274333882308138)


if __name__ == '__main__':
    unittest.main(verbosity=2)
