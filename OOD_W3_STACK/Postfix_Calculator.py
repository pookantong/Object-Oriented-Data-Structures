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
        return self.items[-1] if not self.isEmpty() else None
    
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