import random
from balance import Balance

class Game:

      # 가위바위보 랜덤 값 리턴
    def __init__(self):
        self.computer_rps = random.randint(1, 3)  # 1: 가위  2: 바위  3: 보

    def getComputerRps(self):
        return self.computer_rps

        #  승패무 결정
    def determineWinOrLose(self, myRps):
        if myRps != self.getComputerRps:
            #  승
            if (myRps == 1 and self.getComputerRps == 3) or (myRps == 2 and self.getComputerRps == 1) or (myRps == 3 and self.getComputerRps == 2):
                result = "win"
            #  패
            else:
                result = "lose"
        #  무
        else:
            result = "draw"
        return result

        # 금액 추가
    def addPrice(self, result):
        self.balance = Balance()
        if result == "win":
            self.balance.winPrice
        elif result == "lose":
            self.balance.losePrice
        elif result == "draw":
            self.balance.drawPrice

