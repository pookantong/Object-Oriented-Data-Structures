print(' *** Divisible number ***')
num = int(input('Enter a positive number : '))
def modEqualZero(num):
    if num <= 0:
        print(f'{num} is OUT of range !!!')
        return 0
    count = 0
    print('Output ==> ', end='')
    for number in range(1, num+1):
        if num%number == 0:
            count+=1
            print(number, end=' ')
    print('')
    print('Total ==>', count)
modEqualZero(num)