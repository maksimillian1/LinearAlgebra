from app.models import Matrix
from numpy import *
import unittest
from random import randint


class MatrixTest(unittest.TestCase):

    def testmatrixAdd(self):
        lst = MatrixTest.getRandMatrix()
        print(lst)
        mat = Matrix(value=lst)
        nmat = matrix(lst)
        self.assertEqual(mat+mat.__Matrix_matrix, nmat+nmat)

    @staticmethod
    def getRandMatrix():
        mat = []
        randSize = randint(0,10)
        for i in range(randSize):
            tmp = []
            for i in range(randSize):
                tmp.append(randint(0,1000))
            mat.append(tmp)
        return mat


if __name__ == '__main__':
    unittest.main()