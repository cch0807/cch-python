import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(1, 2)
        self.assertEqual(result, 3)

    def test_add2(self):
        result = calc.add(0, -1)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()