num = int(input("Enter Input : "))
loop = (num*2 + 4)//2


for vertical1 in range(loop):
    
    # reverse pyramid dot
    print('.'*(loop-vertical1-1), end='')
    print('#'*(vertical1+1), end='')
        
    # block
    if vertical1 == 0 or vertical1 == loop-1:
        print('+'*loop)
    else:
        print('+' + ('#'*num) + '+')

for vertical2 in range(loop):
    
    # block
    if vertical2 == 0 or vertical2 == loop-1:
        print('#'*loop, end='')
    else:
        print('#' + ('+'*num) + '#', end='')
    
    # reverse pyramid dot
    print('+'*(loop-vertical2), end='')
    print('.'*(vertical2))