def sumEqualFive(numList):
    if len(numList) < 3:
        return 'Array Input Length Must More Than 2'
    result = []
    for i in range(len(numList)):
        for j in range(i+1, len(numList)):
            for k in range(j+1, len(numList)):
                fiveList = [numList[i], numList[j], numList[k]]
                fiveList.sort()
                if numList[i] + numList[j] + numList[k] == 5 and set(fiveList) not in [set(x) for x in result]:
                    result.append(fiveList)
    return result


numList = [int(x) for x in input('Enter Your List : ').split()]

print(sumEqualFive(numList))