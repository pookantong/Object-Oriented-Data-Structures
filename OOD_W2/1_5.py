print('*** TorKham HanSaa ***')

orders = input('Enter Input : ').split(',')
khamList = []
for order in orders:
    orderSplit = order.split()
    if orderSplit[0] == 'P':
        kham = orderSplit[1]
        if len(khamList) == 0:
            khamList.append(kham)
            print(f'\'{kham}\' -> {khamList}')
        elif kham[:2].lower() == khamList[-1][-2:].lower():
            khamList.append(kham)
            print(f'\'{kham}\' -> {khamList}')
        else:
            print(f'\'{kham}\' -> game over')
            
    elif orderSplit[0] == 'R':
        print('game restarted')
        khamList = []
    elif orderSplit[0] == 'X':
        break
    else:
        print(f'\'{order}\' is Invalid Input !!!')
        break