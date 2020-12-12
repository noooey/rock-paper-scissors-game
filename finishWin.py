import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QDialog
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPixmap


class Finish_Win(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pic_win = QPixmap('winloopy.jpg')
        pic = pic_win.scaled(260, 260, Qt.KeepAspectRatio, Qt.FastTransformation)

        pic_label = QLabel(self)
        pic_label.setPixmap(pic)
        #pic_label.setAlignment(Qt.AlignCenter)

        btn_close = QPushButton('모찌롤 와앙~', self)
        btn_close.setStyleSheet('color:white; background:blue')
        btn_close.clicked.connect(QCoreApplication.instance().quit)

        layout = QVBoxLayout()
        layout.addWidget(pic_label)
        layout.addWidget(btn_close)

        self.setLayout(layout)

        self.setWindowTitle('Rock-Paper-Scissors Game')
        self.resize(260, 360)
        self.show()


    def outputFinishWindow(self):
        return super().exec_()

    def disable_btn(self):
        self.checkResultButton.setEnabled(False)



if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Finish_Win()
    sys.exit(app.exec_())