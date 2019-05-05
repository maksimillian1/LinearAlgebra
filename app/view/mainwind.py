import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QPushButton, QFormLayout, QGridLayout, \
    QDesktopWidget


class MainWindow(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.fieldsdict = {}

        position = [(i, j) for i in range(2) for j in range(2)]
        for i, pos in zip(range(4), position):
            line = QLineEdit()
            self.fieldsdict[i] = line
            self.grid.addWidget(line, *pos)

        btn = QPushButton("Get value")
        self.grid.addWidget(btn, 2, 0)
        btn.clicked.connect(self.btnClicked)

        self.resize(300, 250)
        self.moveCenter()
        self.setLayout(self.grid)

    def moveCenter(self):
        geom = self.frameGeometry()
        cnt = QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cnt)
        self.move(geom.topLeft())

    def btnClicked(self):
        self.dlst = []
        tmp = []
        for i in range(len(self.fieldsdict)):
            value = self.fieldsdict[i].text()
            tmp.append(int(value))
            if len(tmp) == 2:
                self.dlst.append(tmp)
                tmp = []
        print(self.dlst)


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()