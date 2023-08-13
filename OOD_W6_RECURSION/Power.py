def power_num(num, power):
    if power == 0:
        return 1
    return power_num(num, power-1) * num

num, power = map(int, input('Enter Input a b : ').split())
print(power_num(num, power))