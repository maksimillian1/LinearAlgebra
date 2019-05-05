from app.models import Matrix
from numpy import *

m1 = [[1, 2],
      [3, 4]]


mt1 = Matrix(value=m1)
mt2 = Matrix(value=m1)


def det2(mat):
    det = (mat[0][0] * mat[1][1]) \
          - (mat[0][1] * mat[1][0])
    return det



def det(mat):
    if len(mat) < 3:
        return det2(mat)
    else:
        res, sign = 0, '+'
        for index in range(len(mat)):
            if sign == '+':
                res += mat[0][index] * det(getMinor(mat, index))
                sign = '-'
            else:
                res += -(mat[0][index] * det(getMinor(mat, index)))
                sign = '+'
    return res


def getMinor(mat, index):
    minor = []
    for i in range(1, len(mat)):
        lst = []
        for j in range(len(mat)):
            if j != index:
                lst.append(mat[i][j])
        minor.append(lst)
    return minor

mat = [[1,2,3], [4,5,6], [7,8,9]]

print(det(mat))

