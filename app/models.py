from app.exceptions import MatrixSizeError
from copy import copy


class Matrix:

    def __init__(self, value):
        self.__matrix = tuple(value)

    def __len__(self):
        return len(self.__matrix)

    def __iter__(self):
        return [i for lst in self.__matrix for i in lst]

    def toList(self):
        lst = []
        for i in self.__matrix:
            lst.append(list(i))
        return lst

    def __repr__(self):
        lst = ""
        for i in range(len(self)):
            lst += "{}\n".format(self.__matrix[i])
        return lst

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__matrix[item]
        elif isinstance(item, list):
            if len(item) == 2:
                return self.__matrix[item[0]][item[1]]
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
        if len(other) != len(self):
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
        self.__matrix = ((value for _ in range(len(self))) for _  in range(len(self)))

    def transpose(self):
        transposed = [[lst[i] for lst in self.__matrix] for i in range(len(self))]
        return Matrix(transposed)

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


class LinearSystemSolver:

    @staticmethod
    def getResult(mat: Matrix, res: list):
        mainDet = float(Matrix.getDet(mat))
        if mainDet != 0:
            resList = []
            for i in range(len(mat)):
                newMat = LinearSystemSolver._changeColMatr(mat, res, i)
                resList.append(float(Matrix.getDet(newMat))/mainDet)
            return resList
        return None

    @staticmethod
    def _changeColMatr(mat: Matrix, col, index):
        toLst = copy(mat).toList()
        for i in range(len(toLst)):
            toLst[i][index] = col[i]
        return Matrix(value=toLst)


class Vector:
    pass