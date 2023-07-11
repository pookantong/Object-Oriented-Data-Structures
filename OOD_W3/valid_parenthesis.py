class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        res = self.items[-1]
        self.items = self.items[:-1]
        return res
    
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)

class Parenthesis:
    def __init__(self):
        self.par = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        self.all_par = ['[','{','(',')','}',']']

    def valid_parenthesis(self, pars):
        stack = Stack()
        for char in pars:
            if char in self.all_par:
                if char in self.par:
                    stack.push(char)
                elif stack.isEmpty():
                    return print(f'{input} close paren excess')
                elif self.par[stack.pop()] != char:
                    return print(f'{input} Unmatch open-close  ')
        if not stack.isEmpty:
            return print(f'{input} open paren excess   {len(stack.items)} : ', *stack.items, sep='')
        return print(f'{input} MATCH')


input = input('Enter expresion : ')
par = Parenthesis()
par.valid_parenthesis(input)