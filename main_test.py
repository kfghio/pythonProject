import unittest
import calc

class Testmain(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calc.sum(10, 5),15)
        self.assertEqual(calc.sum(-1, 0), -1)
        self.assertEqual(calc.sum(0, 0), 0)
        self.assertEqual(calc.sum(1, 1), 2)
        self.assertEqual(calc.sum(-1, -1), -2)

    def test_dif(self):
        self.assertEqual(calc.dif(10, 5),5)
        self.assertEqual(calc.dif(-1, 0), -1)
        self.assertEqual(calc.dif(0, 0), 0)
        self.assertEqual(calc.dif(1, 1), 0)
        self.assertEqual(calc.dif(-1, -1), 0)

    def test_res(self):
        self.assertEqual(calc.res(10, 5),50)
        self.assertEqual(calc.res(-1, 0), 0)
        self.assertEqual(calc.res(0, 0), 0)
        self.assertEqual(calc.res(1, 1), 1)
        self.assertEqual(calc.res(-1, -1), 1)

    def test_dl(self):
        self.assertEqual(calc.dl(10, 5),2)
        self.assertEqual(calc.dl(-1, 0), 0)
        self.assertEqual(calc.dl(0, 0), 0)
        self.assertEqual(calc.dl(1, 1), 1)
        self.assertEqual(calc.dl(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()