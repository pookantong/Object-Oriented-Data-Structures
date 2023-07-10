print('*** New Range ***')

def manualRange(arg1, arg2=None, arg3=1):
    result = []
    if not arg2:
        start = 0.0 
        stop = arg1
        while start < stop:
            result.append(start)
            start+=1
    else:
        start = arg1
        stop = arg2
        step = arg3
        while start < stop:
            result.append(start)
            start+=step
    return [round(x, 3) for x in result]

argument = [float(x) for x in input('Enter Input : ').split()]
print('(', end='')
print(*manualRange(*argument), sep=', ', end='')
print(')')
