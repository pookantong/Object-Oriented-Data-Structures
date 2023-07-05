print('*** New Range ***')

def manualRange(argument):
    result = []
    if len(argument) == 1:
        start = 0.0
        stop = argument[0]
        while start < stop:
            result.append(start)
            start+=1
    elif len(argument) == 2:
        start = argument[0]
        stop = argument[1]
        while start < stop:
            result.append(start)
            start+=1
    elif len(argument) == 3:
        start = argument[0]
        stop = argument[1]
        step = argument[2]
        while start < stop:
            result.append(start)
            start+=step
    return [round(x, 3) for x in result]

argument = [ float(x) for x in input('Enter Input : ').split()]
print('(', end='')
print(*manualRange(argument), sep=', ', end='')
print(')')