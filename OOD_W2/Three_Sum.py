def sumEqualFive(numList, tripNum, result):
    if len(tripNum) == 3 and sum(tripNum) == 5 and set(tripNum) not in [set(x) for x in result]:
        tripNum.sort()
        result.append(tripNum)
        return
    elif len(tripNum) == 3 or not numList:
        return
    
    sumEqualFive(numList[1:], tripNum + [numList[0]], result)
    sumEqualFive(numList[1:], tripNum, result)

numList = [int(x) for x in input('Enter Your List : ').split()]
result = []
tripNum = []
if len(numList) < 3:
        print('Array Input Length Must More Than 2')
else:
    sumEqualFive(numList, tripNum, result)
    print(result)
