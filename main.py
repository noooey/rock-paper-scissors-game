from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTextEdit, QToolButton, QLabel, QDialog, QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtGui import QPixmap

from logic import Game
from finishWin import Finish_Win
from finishLose import Finish_Lose
from balance import Balance


<<<<<<< HEAD
class Button(QPushButton):
=======
class Button(QToolButton):
>>>>>>> 102302e6506ea459d58635629b1e3be42596650d

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 50)
        size.setWidth(max(size.width(), size.height()))
        return size


class RPSGame(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Rock-Paper-Scissors Layout creation
        rpsLayout = QGridLayout()

        # Balance display window
        self.balance = Balance()
        self.balanceWindow = QTextEdit()
        self.balanceWindow.setMaximumHeight(30)  # 세로 길이 수정
        self.balanceWindow.setMaximumWidth(80)
        self.balanceWindow.setReadOnly(True)
        self.balanceWindow.setAlignment(Qt.AlignCenter)
        rpsLayout.addWidget(self.balanceWindow, 0, 2, 1, 1)

        # 위에 결과 출력
        self.resultWindow2 = QTextEdit()  # 결과를 출력하는 페이지, 추후 이미지를 넣을지 글자만 넣을지 결정
        self.resultWindow2.setMaximumHeight(30)  # 세로 길이 수정
        self.resultWindow2.setMaximumWidth(80)
        self.resultWindow2.setReadOnly(True)  # 연결을 읽기 전용으로 함
        self.resultWindow2.setAlignment(Qt.AlignCenter)
        rpsLayout.addWidget(self.resultWindow2, 0, 0, 1, 1)

        self.balanceLabel = QLabel()
        self.balanceLabel.setText('               잔액:')
        rpsLayout.addWidget(self.balanceLabel, 0, 1, 1, 1)

        '''
        # Result display window
        self.resultWindow = QTextEdit()  # 결과를 출력하는 페이지, 추후 이미지를 넣을지 글자만 넣을지 결정
        self.resultWindow.setReadOnly(True)  # 연결을 읽기 전용으로 함
        self.resultWindow.setAlignment(Qt.AlignCenter)
        rpsLayout.addWidget(self.resultWindow, 1, 0, 1, 3)        
        '''
        self.picWindow = QLabel()
        pic_basic = QPixmap('IMG-0017.JPG')
        pic = pic_basic.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.picWindow.setPixmap(pic)
        rpsLayout.addWidget(self.picWindow, 1, 0, 1, 3)


        # Rock Button
        self.rockButton = Button('바위', self.rockButtonClicked)  # 추후 이미지로 설정
        self.rockButton.setStyleSheet('color:white; background:red')
        rpsLayout.addWidget(self.rockButton, 2, 1, 1, 1)

        # Paper Button
        self.paperButton = Button('보', self.paperButtonClicked)
        self.paperButton.setStyleSheet('color:white; background:green')
        rpsLayout.addWidget(self.paperButton, 2, 2, 1, 1)

        # Scissors Button
        self.scissorsButton = Button('가위', self.scissorsButtonClicked)
        self.scissorsButton.setStyleSheet('color:white; background:blue')
        rpsLayout.addWidget(self.scissorsButton, 2, 0, 1, 1)

        # Button for check the result
        self.checkResultButton = Button('결과 확인하기', self.checkResultButtonClicked)
        self.checkResultButton.setEnabled(False)
        self.checkResultButton.setMaximumHeight(30)  # 세로 길이 수정
        rpsLayout.addWidget(self.checkResultButton, 3, 0, 1, 3)

        # window output
        rpsLayout.setSizeConstraint(QLayout.SetFixedSize)  # 사이즈 고정
        self.setLayout(rpsLayout)
        self.setWindowTitle("Rock-Paper-Scissors Game")


    def setGame(self):
        self.balance = Balance()
        self.balanceWindow.setPlaceholderText(str(self.balance.currentBalance()))  # 금액 띄우기

     #  연결 된 창 띄우기
    def outputMainWindow(self):
        return super().exec_()

    #  바위 버튼 눌렀을 때 이벤트 처리
    def rockButtonClicked(self):
        self.goResult(2)

    #  보 버튼 눌렀을 때 이벤트 처리
    def paperButtonClicked(self):
        self.goResult(3)

    #  가위 버튼 눌렀을 때 이벤트 처리
    def scissorsButtonClicked(self):
        self.goResult(1)

     #  결과 산출 메소드
    def goResult(self, rps):
        self.game = Game()
        self.balance.deductPrice()

<<<<<<< HEAD
        if self.game.determineWinOrLose(rps) == "win":
            self.resultWindow.setPlaceholderText("win")
            self.balance.winPrice()

        elif self.game.determineWinOrLose(rps) == "lose":
            self.resultWindow.setPlaceholderText("lose")
            self.balance.losePrice()

        elif self.game.determineWinOrLose(rps) == "draw":
            self.resultWindow.setPlaceholderText("draw")
            self.balance.drawPrice()

=======
        # 승
        if self.game.determineWinOrLose(rps) == "youS_comP_win":
            self.resultWindow2.setPlaceholderText("win")
            pic_win = QPixmap('IMG-0014.JPG')
            pic = pic_win.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picWindow.setPixmap(pic)
            self.balance.winPrice()
        elif self.game.determineWinOrLose(rps) == "youR_comS_win":
            self.resultWindow2.setPlaceholderText("win")
            pic_win = QPixmap('IMG-0007.JPG')
            pic = pic_win.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picWindow.setPixmap(pic)
            self.balance.winPrice()
        elif self.game.determineWinOrLose(rps) == "youP_comR_win":
            self.resultWindow2.setPlaceholderText("win")
            pic_win = QPixmap('IMG-0011.JPG')
            pic = pic_win.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picWindow.setPixmap(pic)
            self.balance.winPrice()
        # 패
        elif self.game.determineWinOrLose(rps) == "youS_comR_lose":
            self.resultWindow2.setPlaceholderText("lose")
            pic_lose = QPixmap('IMG-0010.JPG')
            pic = pic_lose.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picWindow.setPixmap(pic)
            self.balance.losePrice()
        elif self.game.determineWinOrLose(rps) == "youR_comP_lose":
            self.resultWindow2.setPlaceholderText("lose")
            pic_lose = QPixmap('IMG-0016.JPG')
            pic = pic_lose.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picWindow.setPixmap(pic)
            self.balance.losePrice()
        elif self.game.determineWinOrLose(rps) == "youP_comS_lose":
            self.resultWindow2.setPlaceholderText("lose")
            pic_lose = QPixmap('IMG-0008.JPG')
            pic = pic_lose.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picWindow.setPixmap(pic)
            self.balance.losePrice()
        # 무
        elif self.game.determineWinOrLose(rps) == "youS_comS_draw":
            self.resultWindow2.setPlaceholderText("draw")
            pic_draw = QPixmap('IMG-0009.JPG')
            pic = pic_draw.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picWindow.setPixmap(pic)
            self.balance.drawPrice()
        elif self.game.determineWinOrLose(rps) == "youR_comR_draw":
            self.resultWindow2.setPlaceholderText("draw")
            pic_draw = QPixmap('IMG-0012.JPG')
            pic = pic_draw.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picWindow.setPixmap(pic)
            self.balance.drawPrice()
        elif self.game.determineWinOrLose(rps) == "youP_youP_draw":
            self.resultWindow2.setPlaceholderText("draw")
            pic_draw = QPixmap('IMG-0015.JPG')
            pic = pic_draw.scaled(260, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picWindow.setPixmap(pic)
            self.balance.drawPrice()


>>>>>>> 102302e6506ea459d58635629b1e3be42596650d
        self.balanceWindow.setPlaceholderText(str(self.balance.currentBalance()))  # 현재 금액 띄우기

        if self.balance.currentBalance() >= 1000:
            self.balanceWindow.setPlaceholderText("1000")
            self.checkResultButton.setEnabled(True)
            self.rockButton.setEnabled(False)
            self.paperButton.setEnabled(False)
            self.scissorsButton.setEnabled(False)
<<<<<<< HEAD
=======
            self.rockButton.setStyleSheet('color:white; background:gray')
            self.paperButton.setStyleSheet('color:white; background:gray')
            self.scissorsButton.setStyleSheet('color:white; background:gray')
>>>>>>> 102302e6506ea459d58635629b1e3be42596650d
        elif self.balance.currentBalance() <= 0:
            self.checkResultButton.setEnabled(True)
            self.rockButton.setEnabled(False)
            self.paperButton.setEnabled(False)
            self.scissorsButton.setEnabled(False)
<<<<<<< HEAD
=======
            self.rockButton.setStyleSheet('color:white; background:gray')
            self.paperButton.setStyleSheet('color:white; background:gray')
            self.scissorsButton.setStyleSheet('color:white; background:gray')

>>>>>>> 102302e6506ea459d58635629b1e3be42596650d

     # 결과 확인하기 버튼 눌렀을 때 이벤트 처리
    def checkResultButtonClicked(self):
        self.close()
        if self.balance.currentBalance() >= 1000:
            self.finishWindow = Finish_Win()
            self.finishWindow.outputFinishWindow()

        elif self.balance.currentBalance() <= 0:
<<<<<<< HEAD
            self.finishWindow = Finish_Win()
=======
            self.finishWindow = Finish_Lose()
>>>>>>> 102302e6506ea459d58635629b1e3be42596650d
            self.finishWindow.outputFinishWindow()

        else:
            return 0


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = RPSGame()
    main.show()
    sys.exit(app.exec_())
