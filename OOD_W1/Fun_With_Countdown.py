print('*** Fun with countdown ***')

def countdown(numList):
    countdownList = []
    stack = []
    for num in numList:
        if len(stack) == 0:
            stack.append(num)
            if num == 1:
                countdownList.append(stack)
                stack = []
        elif num == 1:
            stack.append(num)
            countdownList.append(stack)
            stack = []
        elif stack[-1] == num+1:
            stack.append(num)
        else:
            stack = [num]
    return [len(countdownList), countdownList]

numList = [int(x) for x in input('Enter List : ').split()]
print(countdown(numList))