import calculator as c
import unittest


class TestSum(unittest.TestCase):

    def test_sum_int(self):
        self.assertEqual(c.sum(1, 2), 3, "Should be 3")

    def test_sum_float(self):
        self.assertEqual(c.sum(1.2, 2.3),3.5,"Should be 3.5")
    
    def test_multiply_int(self):
        self.assertEqual(c.multiply(2, 3),6,"Should be 6")
    
    def test_multiply_float(self):
        self.assertEqual(c.multiply(1.2, 2.3),2.76,"Should be 2.76")

    def test_divide_int(self):
        self.assertEqual(c.divide(12, 3),4,"Should be 4")

    def test_divide_float(self):
        self.assertEqual(c.divide(10, 2.5),4,"Should be 4")

    def test_minus_int(self):
        self.assertEqual(c.minus(10, 2),8,"Should be 8")

    def test_minus_float(self):
        self.assertEqual(c.minus(10, 2.5),7.5,"Should be 7.5")
    

if __name__ == "__main__":
    unittest.main()