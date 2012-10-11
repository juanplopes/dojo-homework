import unittest
from miojo import miojo

class TestMiojo(unittest.TestCase):
    def test_3_5_7(self):
        self.assertEqual(10, miojo(3, 5, 7))

    def test_14_15_22(self):
        self.assertEqual(44, miojo(14, 15, 22))

    def test_1_2_3(self):
        self.assertEqual(3, miojo(1, 2, 3))
        
    def test_1_4_3(self):
        self.assertEqual(4, miojo(1, 4, 3))

    def test_4_5_7(self):
        self.assertEqual(14, miojo(4, 5, 7))

    def test_4_2_3(self):
        self.assertEqual(4, miojo(4, 2, 3))

unittest.main()
