class Queue:
    def __init__(self) -> None:
        self.__items = []
        
    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0) if not self.isEmpty() else -1

    def isEmpty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)
    
    @property
    def items(self):
        return self.__items

inputs = input("Enter Input : ").split(',')
queue = Queue()
for inp in inputs:
    command = inp.split()
    if command[0] == 'E':
         queue.enqueue(command[1])
         print(f'Add {command[1]} index is {queue.size()-1}')
    else:
        if not queue.isEmpty():
            print(f'Pop {queue.dequeue()} size in queue is {queue.size()}')
        else:
            print(queue.dequeue())
if queue.isEmpty():
    print('Empty')
else:
    print(f'Number in Queue is :  {queue.items}')