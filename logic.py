import random

class gameLogic:

     #  잔액 100원 차감, 가위 바위 보 랜덤 값 리턴
    def setGame(self, bal):
        bal -= 100
        computer_rps = random.randint(1, 3)  # 1: 가위  2: 바위  3: 보
        return computer_rps


     #  게임 메인 로직 구현
    def mainLogic(self, myRps, com_rps, bal):

        if myRps != com_rps:
             #  승
            if (myRps == 1 and com_rps == 3) or (myRps == 2 and com_rps == 1) or (myRps == 3 and com_rps == 2):
                bal += self.randomPrice
                result = "win"
             #  패
            else:
                 bal += 0
                 result = "lose"
         #  무
        else:
            bal += 100
            result = "draw"
        return result

     #  100~500원 랜덤 금액 설정
    def randomPrice(self):
        return random.randint(1, 5)*100
