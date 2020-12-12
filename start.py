import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from main import RPSGame


class Start(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pic_start = QPixmap('startloopy.jpg')
        pic = pic_start.scaled(290, 290, Qt.KeepAspectRatio, Qt.FastTransformation)

        pic_label = QLabel(self)
        pic_label.setPixmap(pic)
        pic_label.setAlignment(Qt.AlignCenter)

        btn = QPushButton('start', self)
        btn.setStyleSheet('color:white; background:orange')
        btn.clicked.connect(self.startButtonClicked)

        layout = QVBoxLayout()
        layout.addWidget(pic_label)
        layout.addWidget(btn)

        self.setLayout(layout)

        self.setWindowTitle("Rock-Paper-Scissors Game")
        self.resize(300, 380)
        self.show()

    def startButtonClicked(self):
        self.close()
        self.mainWindow = RPSGame()
        self.mainWindow.setGame()
        self.mainWindow.outputMainWindow()

        #  연결 된 창 띄우기
    def outputStartWindow(self):
        return super().exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = Start()
    start.show()
    app.exec()