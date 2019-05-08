import sys
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget, QDesktopWidget, QButtonGroup
from app.view.matrix_window import MatrixWindow
from app.view.QtFeatures import moveCenter


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.defaultSize = (300, 150)
        self.vbox = QVBoxLayout()
        self.vector = QPushButton('Vectors')
        self.matrix = QPushButton('Matrix Calc')
        self.system = QPushButton('Linear systems')
        self.btns = ((0, self.vector), (1, self.matrix), (2, self.system))
        self.btnGroup = QButtonGroup()
        self.choice = None
        self.initUI()

    def initUI(self):
        for item in self.btns:
            self.btnGroup.addButton(item[1], item[0])
            self.vbox.addWidget(item[1])

        self.btnGroup.buttonClicked[int].connect(self.buttonsClicked)

        self.resize(*self.defaultSize)
        self.setMaximumSize(*self.defaultSize)
        self.setLayout(self.vbox)
        self.setWindowTitle("Linear Algebra")
        moveCenter(self)


    def buttonsClicked(self, id):
        print(id)
        if id == 0:
            pass
        elif id == 1:
            self.choice = MatrixWindow()
            self.choice.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = MainWindow()
    wind.show()
    sys.exit(app.exec_())