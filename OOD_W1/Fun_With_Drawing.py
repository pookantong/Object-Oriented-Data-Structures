#algo for 4 quadrant
print('*** Fun with Drawing ***')
num = int(input('Enter input : '))
num = (num-1)*2+1
for vertical in range(num):
    for horizontal in range(num): #start with q2
        if vertical%2 == 0: 
            if horizontal%2!=0 and vertical>horizontal:
                print('.', end='')    
            else:
                print('#', end='')
        else:
            if horizontal%2==0 and vertical>horizontal:
                print('#', end='')    
            else:
                print('.', end='')
    for horizontal in range(num-1, 0, -1): #q1
        if vertical%2 == 0: 
            if horizontal%2==0 and vertical>=horizontal:
                print('.', end='')    
            else:
                print('#', end='')
        else: 
            if horizontal%2!=0 and vertical>=horizontal:
                print('#', end='')    
            else:
                print('.', end='')
    print('')
for vertical in range(num-2, -1, -1):
    for horizontal in range(num): #q3
        if vertical%2 == 0: 
            if horizontal%2!=0 and vertical>horizontal:
                print('.', end='')    
            else:
                print('#', end='')
        else:
            if horizontal%2==0 and vertical>horizontal:
                print('#', end='')    
            else:
                print('.', end='')
    for horizontal in range(num-1, 0, -1): #q4
        if vertical%2 == 0: 
            if horizontal%2==0 and vertical>=horizontal:
                print('.', end='')    
            else:
                print('#', end='')
        else: 
            if horizontal%2!=0 and vertical>=horizontal:
                print('#', end='')    
            else:
                print('.', end='')
    print('')