from PyQt5.QtWidgets import QWidget, QLineEdit, QButtonGroup, QPushButton, QGridLayout, QDesktopWidget, \
    QVBoxLayout, QComboBox, QApplication, QLabel
from app.view.QtFeatures import moveCenter
from app.models import *
import sys


class LinearSystemWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.fields = []
        self.equalField = []
        self.vars = ('x1', 'x2', 'x3', 'x4')
        self.sizes = (2, 3, 4)
        self.sizeBox = QComboBox()
        self.solve = QPushButton("Solve")
        self.resLabel = QLabel()
        self.valuesGrid = QGridLayout()
        self.mainLayout = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.mainLayout.addWidget(self.sizeBox)
        self.mainLayout.addLayout(self.valuesGrid)
        self.mainLayout.addWidget(self.solve)
        self.mainLayout.addWidget(self.resLabel)
        [self.sizeBox.addItem(str(item)) for item in self.sizes]
        self.makeGrid('2')
        self.sizeBox.activated[str].connect(self.makeGrid)

        self.solve.clicked.connect(self.clickedSolve)
        moveCenter(self)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("Linear equation system solver")

    def makeGrid(self, size):
        self.fields.clear()
        self.equalField.clear()
        if self.valuesGrid.count() > 0:
            for i in reversed(range(self.valuesGrid.count())):
                self.valuesGrid.itemAt(i).widget().setParent(None)

        rawWidgect = self.generateRaw(size)
        pos = [(x, y) for x in range(int(size)) for y in range(int(len(rawWidgect)/int(size)))]
        for wg, i, ps in zip(rawWidgect, range((len(rawWidgect))), pos):
            if isinstance(wg, QLineEdit):
                if wg.placeholderText() == 'y':
                    self.equalField.append(wg)
                self.fields.append(wg)
            self.valuesGrid.addWidget(wg, *ps)
        print(self.equalField)
        print(self.fields)


    def generateRaw(self, size):
        labels = []
        for i in range(int(size)):
            for i in range(0, int(size)):
                labels.append(QLineEdit())
                labels.append(QLabel("x{}".format(i+1)))
            labels.append(QLabel("="))
            y = QLineEdit()
            y.setPlaceholderText('y')
            labels.append(y)
        return labels

    def clickedSolve(self):
        systemSize = int(self.sizeBox.currentText())
        mat = []
        vals = []
        index = 0
        try:
            for i in range(systemSize):
                tmp = []
                vals.append(int(self.equalField[i].text()))
                for j in range(systemSize):
                    tmp.append(int(self.fields[index].text()))
                    index +=1
                mat.append(tmp)

            res = LinearSystemSolver.getResult(Matrix(mat), vals)
            self.resLabel.setText(self._renderResult(res))
        except ValueError:
            self.setStatusTip("Enter valid numbers!")

    def _renderResult(self, lst):
        if lst is None:
            return "Set of solution"
        rendered = ""
        for i in range(len(lst)):
            rendered += "{}={}\n".format(self.vars[i], lst[i])
        return rendered
