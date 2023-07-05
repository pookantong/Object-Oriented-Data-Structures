print('*** String Rotation ***')
str1, str2 = input('Enter 2 strings : ').split()
loopStr1 = str1[-2:] + str1[:-2]
loopStr2 = str2[3:] + str2[:3]
count = 1
while loopStr1 != str1 or loopStr2 != str2:
    if count <= 5:
        print(count, loopStr1, loopStr2)
    loopStr1 = loopStr1[-2:] + loopStr1[:-2]
    loopStr2 = loopStr2[3:] + loopStr2[:3]
    count+=1
if count > 5:
    print(' . . . . . ')
print(count, loopStr1, loopStr2)
print(f'Total of  {count} rounds.')