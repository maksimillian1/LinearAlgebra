from app.models import Matrix


a = Matrix(4)
a.fillwith(4)

a[2] = 1,2,3,4
print(a)