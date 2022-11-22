import random

class Game:

      # 가위바위보 랜덤 값 리턴
    def __init__(self):
          self.computer_rps = random.randint(1, 3)  # 1: 가위  2: 바위  3: 보

    def getComputerRps(self):
        return self.computer_rps

<<<<<<< HEAD
        #  승패무 결정
    def determineWinOrLose(self, myRps):
=======
    ''' #  승패무 결정
        def determineWinOrLose(self, myRps):
>>>>>>> 102302e6506ea459d58635629b1e3be42596650d
        if myRps != self.getComputerRps():
            #  승
            if (myRps == 1 and self.getComputerRps() == 3) or (myRps == 2 and self.getComputerRps() == 1) or (myRps == 3 and self.getComputerRps() == 2):
                result = "win"
            #  패
            else:
                result = "lose"
        #  무
        else:
            result = "draw"
<<<<<<< HEAD
=======
        return result
    '''
    def determineWinOrLose(self, myRps):    # 1: 가위  2: 바위  3: 보
        # 승
        if myRps == 1 and self.getComputerRps() == 3:
            result = "youS_comP_win"
        elif myRps == 2 and self.getComputerRps() == 1:
            result = "youR_comS_win"
        elif myRps == 3 and self.getComputerRps() == 2:
            result = "youP_comR_win"
        # 패
        elif myRps == 1 and self.getComputerRps() == 2:
            result = "youS_comR_lose"
        elif myRps == 2 and self.getComputerRps() == 3:
            result = "youR_comP_lose"
        elif myRps == 3 and self.getComputerRps() == 1:
            result = "youP_comS_lose"
        # 무
        elif myRps == 1 and self.getComputerRps() == 1:
            result = "youS_comS_draw"
        elif myRps == 2 and self.getComputerRps() == 2:
            result = "youR_comR_draw"
        elif myRps == 3 and self.getComputerRps() == 3:
            result = "youP_youP_draw"

>>>>>>> 102302e6506ea459d58635629b1e3be42596650d
        return result