import unittest
from distance import distance_1

class test1 (unittest.TestCase):

    def test_zero(self):
        res = distance_1(2, 4, 5, 6)
        self.assertEqual(res, 6.5)

    def test_one(self):
        res = distance_1(0,0,1,1)
        self.assertEquals(res, 2**0.5)

if __name__ == "__main__":
    unittest.main()