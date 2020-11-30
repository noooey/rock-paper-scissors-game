import random

class Balance:

    def __init__(self):
        self.balance = 300

    def deductPrice(self):
        self.balance -= 100

    def winPrice(self):
        self.balance += self.randomPrice()

    def losePrice(self):
        self.balance += 0

    def drawPrice(self):
        self.balance += 100

    def currentBalance(self):
        return self.balance

        #  100~500원 랜덤 금액 설정
    def randomPrice(self):
         return random.randint(1, 5) * 100