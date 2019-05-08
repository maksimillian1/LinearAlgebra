from app.models import Matrix
from numpy import *
import unittest
from random import randint


class MatrixTest(unittest.TestCase):

    def MatrixAdd(self):
        lst = MatrixTest.getRandMatrix()
        mat = Matrix(value=lst)
        nmat = matrix(lst)
        self.assertEqual((mat+mat).toList(), (nmat+nmat).tolist())

    def testAdd100Times(self):
        for i in range(100):
            self.MatrixAdd()

    def MatrixSub(self):
        lst = MatrixTest.getRandMatrix()
        mat = Matrix(value=lst)
        nmat = matrix(lst)
        self.assertEqual((mat - mat).toList(), (nmat - nmat).tolist())

    def testSub100Times(self):
        for i in range(100):
            self.MatrixSub()

    def MatrixMul(self):
        lst = MatrixTest.getRandMatrix()
        mat = Matrix(value=lst)
        nmat = matrix(lst)
        self.assertEqual((mat * mat).toList(), (nmat * nmat).tolist())

    def testMul10Times(self):
        for i in range(100):
            self.MatrixMul()

    @staticmethod
    def getRandMatrix():
        mat = []
        randSize = randint(1,1000)
        for i in range(randSize):
            tmp = []
            for i in range(randSize):
                tmp.append(randint(1,1000))
            mat.append(tmp)
        return mat


if __name__ == '__main__':
    unittest.main()