def asteroid_collision(asts, index=0):
    if len(asts) == index:
        return asts
    elif index == 0:
        return asteroid_collision(asts, index+1)
    elif asts[index] < 0 and asts[index-1] > 0:
        if abs(asts[index]) > asts[index-1]:
            asts.pop(index-1)
        elif abs(asts[index]) < asts[index-1]:
            asts.pop(index)
        elif abs(asts[index]) == asts[index-1]:
            asts.pop(index)
            asts.pop(index-1)
        return asteroid_collision(asts)
    return asteroid_collision(asts, index+1)

x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x))