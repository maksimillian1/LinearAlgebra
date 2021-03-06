from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QGridLayout, \
    QDesktopWidget, QComboBox, QLabel
from app.models import Matrix
from app.view.QtFeatures import moveCenter


class MatrixWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout()
        self.first_grid = QGridLayout()
        self.second_grid = QGridLayout()
        self.resuld_grid = QGridLayout()
        self.chose_sign, self.chose_size = QComboBox(), QComboBox()
        self.firstField, self.secondField = {}, {}
        self.size = 0
        self.initUI()

    def initUI(self):
        btn = QPushButton("Get value")

        self.chose_size.addItems(['2','3','4'])
        self.chose_sign.addItems(['+','-','*'])
        self.onActivated(2)
        self.chose_size.activated[str].connect(self.onActivated)
        self.main_layout.addWidget(self.chose_size)

        self.main_layout.addLayout(self.first_grid)
        self.main_layout.addWidget(self.chose_sign)
        self.main_layout.addLayout(self.second_grid)
        self.main_layout.addWidget(btn)
        self.main_layout.addLayout(self.resuld_grid)

        btn.clicked.connect(self.btnClicked)
        moveCenter(self)
        self.setLayout(self.main_layout)

    def onActivated(self, size):
        self.size = int(size)
        self.firstField.clear()
        self.createTable(self.first_grid, self.firstField)
        self.createTable(self.second_grid, self.secondField)

    def createTable(self, grid, fields):
        self.clearIfNotEmpty(grid)
        position = [(i, j) for i in range(self.size) for j in range(self.size)]
        for i, pos in zip(range(self.size*self.size), position):
            line = QLineEdit()
            line.setFixedSize(50, 35)
            fields[i] = line
            grid.addWidget(line, *pos)

    def getMatrix(self, grid):
        matrix, tmp = [], []
        for i in range(len(grid)):
            value = grid[i].text()
            tmp.append(int(value))
            if len(tmp) == self.size:
                matrix.append(tmp)
                tmp = []
        return Matrix(value=matrix)

    def btnClicked(self):
        m1 = self.getMatrix(self.firstField)
        m2 = self.getMatrix(self.secondField)
        sign = self.chose_sign.currentText()
        if sign == '+':
            self.showResult(m1 + m2)
        elif sign == '*':
            self.showResult(m1 * m2)
        else:
            self.showResult(m1 - m2)
        self.clearIfNotEmpty(self.first_grid)
        self.clearIfNotEmpty(self.second_grid)

    def showResult(self, matrix):
        if self.resuld_grid.count() > 0:
            for i in reversed(range(self.resuld_grid.count())):
                self.resuld_grid.itemAt(i).widget().setText("")

        pos = ((i, j) for i in range(len(matrix)) for j in range(len(matrix)))
        for ps in pos:
            lab = QLabel(str(matrix[ps[0], ps[1]]))
            self.resuld_grid.addWidget(lab, *ps)

    def clearIfNotEmpty(self, grid):
        if grid.count() > 0:
            for i in reversed(range(grid.count())):
                grid.itemAt(i).widget().setText("")