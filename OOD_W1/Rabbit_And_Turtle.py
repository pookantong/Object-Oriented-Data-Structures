print('*** Rabbit & Turtle ***')
d, vr, vt, vf = [int(x) for x in input("Enter Input : ").split()]
t = d/(vt-vr)
ans = vf*t
print(f'{ans:.2f}')