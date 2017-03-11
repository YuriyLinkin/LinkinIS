import unittest
from llll import ITEmployee

class EmpNoPositionTests(unittest.TestCase):
    def test_creation(self):
        emp = ITEmployee('Root', 'QA')
        self.assertEqual(emp.name, 'Root')
        self.assertEqual(emp.position, 'QC')
        #self.assertEqual(emp.surname, None)
        self.assertEqual(len(emp.skills), 0)


    # def test_wrong_creation(self):
    #     ITEmployee("Root")


# class PositiveTests (unittest.TestCase):
#     pass


if __name__ == "__main__":
    unittest.main()