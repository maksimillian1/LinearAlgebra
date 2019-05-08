from PyQt5.QtWidgets import QWidget, QLineEdit, QButtonGroup, QPushButton, QGridLayout, QDesktopWidget, \
    QVBoxLayout, QComboBox, QApplication
from app.view.QtFeatures import moveCenter
import sys

class LinearSystemWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.fields = []
        self.equalField = []
        self.sizes = (2, 3, 4)
        self.sizeBox = QComboBox()
        self.solve = QPushButton()
        self.valuesGrid = QGridLayout()
        self.mainLayout = QVBoxLayout()


        self.initUI()

    def initUI(self):
        self.mainLayout.addWidget(self.sizeBox)
        self.mainLayout.addLayout(self.valuesGrid)
        self.mainLayout.addWidget(self.solve)
        [self.sizeBox.addItem(str(item)) for item in self.sizes]
        self.sizeBox.activated[str].connect(self.makeGrid)

        self.solve.clicked.connect(self.clickedSolve)
        moveCenter(self)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("Linear equation system solver")

    def makeGrid(self, size):
        print(self.size())
        if self.valuesGrid.count() > 0:
            for i in reversed(range(self.valuesGrid.count())):
                self.valuesGrid.itemAt(i).widget().setParent(None)

        pos = [(x, y) for x in range(int(size)) for y in range(int(size)+1)]
        for i, ps in zip(range((int(size)+1)*int(size)), pos):
            line = QLineEdit()
            line.setFixedSize(50, 35)
            self.valuesGrid.addWidget(line, *ps)
            if (i + 1) % int(size):
                self.equalField.append(line)
            else:
                self.fields.append(line)

    def clickedSolve(self):
        systemSize = int(self.sizeBox.currentText())
        size = int(len(self.fields)/systemSize)
        mat = []
        vals = []
        index = 0
        for i in range(size):
            tmp = []
            vals.append(int(self.equalField[i].text()))
            for j in range(size):
                tmp.append(int(self.fields[index].text()))
                index +=1
            mat.append(tmp)
        print(mat)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = LinearSystemWindow()
    wnd.show()
    sys.exit(app.exec_())