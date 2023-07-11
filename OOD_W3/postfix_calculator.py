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
        if len(self.items) == 0:
            return True
        return False
    
    def size(self):
        return len(self.items)

def postFixeval(st):
    operators = ['+','-','*','/']
    s = Stack()
    for char in st:
        if char not in operators:
            num = int(char)
            s.push(num)
        else:
            num2 = s.pop()
            num1 = s.pop()
            if char == '+':
                s.push(num1+num2)
            elif char == '-':
                s.push(num1-num2)
            elif char == '*':
                s.push(num1*num2)
            elif char == '/':
                s.push(num1/num2)
    return s.pop()

print(" ***Postfix expression calcuation***")
token = input("Enter Postfix expression : ").split()
print("Answer : ",'{:.2f}'.format(postFixeval(token)))