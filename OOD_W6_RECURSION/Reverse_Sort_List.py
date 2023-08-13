def reverseSortList(nums):
    if len(nums) == 1:
        return nums
    max_num = max(nums)
    nums.remove(max_num)
    return [max_num] + reverseSortList(nums)

nums = list(map(int, input('Enter your List : ').split(',')))
print(f'List after Sorted : {reverseSortList(nums)}')