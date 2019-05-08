from PyQt5.QtWidgets import QDesktopWidget


def moveCenter(self):
    geom = self.frameGeometry()
    cnt = QDesktopWidget().availableGeometry().center()
    geom.moveCenter(cnt)
    self.move(geom.topLeft())