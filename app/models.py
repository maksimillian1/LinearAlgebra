
class Matrix:

    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def __len__(self):
        return self.size

    def __repr__(self):
        lst = ""
        for i in range(len(self)):
            lst += "{}\n".format(self.matrix[i])
        return lst

    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, item, value):
        self.matrix[item] = value

    def fillwith(self, value):
        self.matrix = [[value for _ in range(len(self))] for _  in range(len(self))]
