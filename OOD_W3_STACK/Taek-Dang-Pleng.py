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


class Plate:
    def __init__(self, weight, freq):
        self.weight = weight
        self.freq = freq


plates = input('Enter Input : ').split(',')
plate_stack = Stack()
for plate in plates:
    cur_plate = Plate(*[int(x) for x in plate.split()])
    while not plate_stack.isEmpty() and cur_plate.weight > plate_stack.peek().weight:
        print(plate_stack.pop().freq)
    plate_stack.push(cur_plate)
        
    
    