def sorting(num_list):
    def insert_sort(numlist, val, index=0):
        if not numlist:
            return [val], index
        elif numlist[0] > val:
            numlist.insert(0, val)
            return numlist, index
        res_list, index_rec = insert_sort(numlist[1:], val, index + 1)
        return [numlist[0]] + res_list, index_rec

    def sorting_(numlist1, numlist2):
        if not numlist2:
            print('sorted')
            return numlist1
        res_list, index = insert_sort(numlist1, numlist2[0])
        if numlist2[1:]:
            print(f'insert {numlist2[0]} at index {index} : {res_list} {numlist2[1:]}')
        else:
            print(f'insert {numlist2[0]} at index {index} : {res_list}')
        return sorting_(res_list, numlist2[1:])

    res_list = sorting_(num_list[:1], num_list[1:])
    return res_list

inp = [int(x) for x in input('Enter Input : ').split()]
print(sorting(inp))