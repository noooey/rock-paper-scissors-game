import random

class gameLogic:

     #  잔액 100원 차감, 가위 바위 보 랜덤 값 리턴
    def setGame(self, bal):
        bal -= 100
        computer_rps = random.random(1, 4)  # 1: 가위  2: 바위  3: 보
        return computer_rps


     #  게임 메인 로직 구현
    def mainLogic(self, rps, computer_rps, bal):

        if rps != computer_rps:
             #  승
            if (rps == 1 and computer_rps == 3) or (rps == 2 and computer_rps == 1) or (rps == 3 and computer_rps == 2):
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
        return random.radom(1, 6)*100
