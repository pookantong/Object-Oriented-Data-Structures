print('*** TorKham HanSaa ***')

class ThorKham:
    def __init__(self) -> None:
        self.khamList = []

    def playGame(self, orders):
        for order in orders:
            orderSplit = order.split()
            if orderSplit[0] == 'P':
                kham = orderSplit[1]
                if len(self.khamList) == 0:
                    self.khamList.append(kham)
                    print(f'\'{kham}\' -> {self.khamList}')
                elif kham[:2].lower() == self.khamList[-1][-2:].lower():
                    self.khamList.append(kham)
                    print(f'\'{kham}\' -> {self.khamList}')
                else:
                    print(f'\'{kham}\' -> game over')
                    
            elif orderSplit[0] == 'R':
                print('game restarted')
                self.khamList = []
            elif orderSplit[0] == 'X':
                break
            else:
                print(f'\'{order}\' is Invalid Input !!!')
                break

orders = input('Enter Input : ').split(',')
ThorKham().playGame(orders)