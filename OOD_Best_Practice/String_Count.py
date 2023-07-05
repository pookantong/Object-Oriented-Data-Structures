print(' *** String count ***')
text = input('Enter message : ')
upperCount = 0
lowerCount = 0
upper = []
lower = []
for char in text:
    if char.islower():
        lowerCount+=1
        if char not in lower:
            lower.append(char)
    elif char.isupper():
        upperCount+=1
        if char not in upper:
            upper.append(char)
upper.sort()
lower.sort()
print('No. of Upper case characters :', upperCount)
print('Unique Upper case characters : ', end ='')
print(*upper, sep='  ', end='')
print('  ')
print('No. of Lower case Characters :', lowerCount)
print('Unique Lower case characters : ', end ='')
print(*lower, sep='  ', end='')
print('  ')
