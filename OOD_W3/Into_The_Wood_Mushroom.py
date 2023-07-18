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
    
class IntoTheWoods:
    
    def __init__(self):
        self.stack = Stack()
        self.cur_stack = Stack()

    # for sort stack and push new item
    def aState(self, new_height):
        while not self.cur_stack.isEmpty() and self.cur_stack.peek() <= new_height:
            self.cur_stack.pop()
        self.cur_stack.push(new_height)
        self.stack.push(new_height)
  
    def bState(self):
        return self.cur_stack.size()
    
    def sState(self):
        temp_stack = Stack()
        # pop to temp_stack with height changed
        while not self.stack.isEmpty():
            if self.stack.peek()%2 == 0:
                temp_stack.push(self.stack.pop()-1)
            else:
                temp_stack.push(self.stack.pop()+2)
        self.cur_stack = Stack()
        # pop back to stack with sort
        while not temp_stack.isEmpty():
            self.stack.push(temp_stack.peek())
            self.aState(temp_stack.pop())

                    
    def count(self, inp):
        act = inp.split()
        act_state = act[0]
        if act_state == 'A':
            self.aState(int(act[1]))
        elif act_state == 'S':
            self.sState()
        else:
            print(self.bState())
                

wood = IntoTheWoods()
inputs = input('Enter Input : ').split(',')
for inp in inputs:
    wood.count(inp)

