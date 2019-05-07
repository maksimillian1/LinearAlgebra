from app.exceptions import MatrixSizeError
import numpy

class Matrix:

    def __init__(self, size=None, value=None):
        if value is not None:
            self.__matrix = value
        else:
            self.__matrix = [[0 for _ in range(size)] for _ in range(size)]

    def __len__(self):
        return len(self.__matrix)

    def __iter__(self):
        return [i for lst in self.__matrix for i in lst]

    def __repr__(self):
        # lst = ""
        # for i in range(len(self)):
        #     lst += "{}\n".format(self.__matrix[i])
        return str(self.__matrix)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__matrix[item]
        elif isinstance(item, list):
            if len(item) == 2:
                return self.__matrix[item[0]][item[1]]
        else:
            raise ValueError

    def __setitem__(self, item, value):
        if isinstance(item, int):
            self.__matrix[item] = list(value)
        elif isinstance(item, tuple):
            if len(item) == 2:
                self.__matrix[item[0]][item[1]] = value
        else:
            raise ValueError

    def __add__(self, other):
        res = []
        for i in range(len(self)):
            tmp = [slf + oth for slf, oth in zip(self[i], other[i])]
            res.append(tmp)
        return Matrix(value=res)

    def __sub__(self, other):
        res = []
        for i in range(len(self)):
            tmp = [slf - oth for slf, oth in zip(self[i], other[i])]
            res.append(tmp)
        return Matrix(value=res)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        if len(other) is not len(self):
            raise MatrixSizeError
        else:
            res = []
            for i in range(len(self)):
                tmp = []
                for j in range(len(self)):
                    num = 0
                    for k in range(len(self)):
                        num += self[i][k] * other[k][j]
                    tmp.append(num)
                res.append(tmp)
            return Matrix(value=res)

    def fillwith(self, value):
        self.__matrix = [[value for _ in range(len(self))] for _  in range(len(self))]

    def transpose(self):
        transposed = [[lst[i] for lst in self.__matrix] for i in range(len(self))]
        return Matrix(value=transposed)

    @staticmethod
    def getDet(mat):
        if len(mat) < 3:
            det = (mat[0][0] * mat[1][1]) \
                  - (mat[0][1] * mat[1][0])
            return det
        else:
            res, sign = 0, '+'
            for index in range(len(mat)):
                if sign == '+':
                    res += mat[0][index] * Matrix.getDet(Matrix.getMinor(mat, index))
                    sign = '-'
                else:
                    res += -(mat[0][index] * Matrix.getDet(Matrix.getMinor(mat, index)))
                    sign = '+'
        return res

    @staticmethod
    def getMinor(mat, index):
        minor = []
        for i in range(1, len(mat)):
            lst = []
            for j in range(len(mat)):
                if j != index:
                    lst.append(mat[i][j])
            minor.append(lst)
        return minor

