class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    

class Parenthesis:
    def __init__(self):
        self.par = {
            ']': '[',
            ')': '('
        }

    def parenthesis_pair(self, pars):
        stack = Stack()
        for par in pars:
            if par in self.par.values():
                stack.push(par)
            elif not stack.isEmpty() and self.par[par] == stack.items[-1]:
                stack.pop()
            else:
                stack.push(par)
            
        print(len(stack.items))
        if stack.isEmpty():
            print('Perfect ! ! !')


input = input('Enter Input : ')
par = Parenthesis()
par.parenthesis_pair(input)