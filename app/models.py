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
    def gauss(A):
        n = len(A)

        for i in range(0, n):
            # Search for maximum in this column
            maxEl = abs(A[i][i])
            maxRow = i
            for k in range(i + 1, n):
                if abs(A[k][i]) > maxEl:
                    maxEl = abs(A[k][i])
                    maxRow = k

            # Swap maximum row with current row (column by column)
            for k in range(i, n + 1):
                tmp = A[maxRow][k]
                A[maxRow][k] = A[i][k]
                A[i][k] = tmp

            # Make all rows below this one 0 in current column
            for k in range(i + 1, n):
                c = -A[k][i] / A[i][i]
                for j in range(i, n + 1):
                    if i == j:
                        A[k][j] = 0
                    else:
                        A[k][j] += c * A[i][j]

        # Solve equation Ax=b for an upper triangular matrix A
        x = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = A[i][n] / A[i][i]
            for k in range(i - 1, -1, -1):
                A[k][n] -= A[k][i] * x[i]
        return x

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
