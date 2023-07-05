def generate_permutations(nums):
    if len(nums) == 1:
        return [nums]
    
    result = []
    for i in range(len(nums)):
        current_num = nums[i]
        remaining_nums = nums[:i] + nums[i+1:]
        permutations = generate_permutations(remaining_nums)
        
        for perm in permutations:
            result.append([current_num] + perm)
    
    return result

def permuFormat(result):
    result.sort(reverse=True)
    format_temp = result[1]
    result[1] = result[3]
    result[3] = format_temp
    return result

numList = [int(x) for x in input().split()]
permutations = generate_permutations(numList)
print(permuFormat(permutations))