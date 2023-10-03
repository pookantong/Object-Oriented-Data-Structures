def sorting(num_list):
    i = 0
    while i != len(num_list):
        for j in range(i+1, len(num_list)):
            if num_list[j] >= 0 and num_list[i] > num_list[j]:
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp
                i = 0
        i+=1
    return num_list

inp = [int(x) for x in input('Enter Input : ').split()]
print(*sorting(inp))