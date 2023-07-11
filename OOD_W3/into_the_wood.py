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
    
class IntoTheWoods:
    
    def __init__(self):
        self.stack = Stack()

    def aState(self, new_height):
        new_stack = Stack()
        for item in self.stack.items:
            if item > new_height:
                new_stack.push(item)
        self.stack = new_stack
        self.stack.push(new_height)
        
    def bState(self):
        return len(self.stack.items)

    def start(self, inp):
        for input in inp:
            act = input.split()
            act_state = act[0]
            if act_state == 'A':
                self.aState(int(act[1]))
            else:
                print(self.bState())
                

woods = IntoTheWoods()
inp = input('Enter Input : ').split(',')
woods.start(inp)

