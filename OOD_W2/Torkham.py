print('*** TorKham HanSaa ***')

class ThorKham:
    def __init__(self) -> None:
        self.khamList = []

    def playGame(self, orders):
        for order in orders:
            orderSplit = order.split()
            if orderSplit[0] == 'P':
                if not self.pState(orderSplit[1]):
                    return     
            elif orderSplit[0] == 'R':
                self.rState()
            elif orderSplit[0] == 'X':
                return
            else:
                print(f'\'{order}\' is Invalid Input !!!')
                return
            
    def pState(self, kham):
        if len(self.khamList) == 0:
            self.khamList.append(kham)
            print(f'\'{kham}\' -> {self.khamList}')
            return True
        elif kham[:2].lower() == self.khamList[-1][-2:].lower():
            self.khamList.append(kham)
            print(f'\'{kham}\' -> {self.khamList}')
            return True
        else:
            print(f'\'{kham}\' -> game over')
            return False
        
    def rState(self):
        print('game restarted')
        self.khamList = []

orders = input('Enter Input : ').split(',')
ThorKham().playGame(orders)