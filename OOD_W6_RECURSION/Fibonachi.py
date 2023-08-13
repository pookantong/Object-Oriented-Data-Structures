def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)


num = int(input('Enter Number : '))
print(f'fibo({num}) = {fibo(num)}')