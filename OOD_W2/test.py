def findSumTriplets(arr, target, triplet, result):
    if len(triplet) == 3 and sum(triplet) == target:
        result.append(triplet)
        return

    if not arr or target < 0:
        return

    findSumTriplets(arr[1:], target, triplet + [arr[0]], result)
    findSumTriplets(arr[1:], target, triplet, result)

arr = [int(x) for x in input().split()]
target = 5
triplet = []
result = []
findSumTriplets(arr, target, triplet, result)
print(result)