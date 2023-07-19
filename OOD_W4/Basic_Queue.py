class Queue:
    def __init__(self) -> None:
        self.__queue = []
        
    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        return self.__queue.pop(0) if not self.isEmpty() else -1

    def isEmpty(self):
        return len(self.__queue) == 0

    def size(self):
        return len(self.__queue)
    
    @property
    def queue(self):
        return self.__queue

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
    print(f'Number in Queue is :  {queue.queue}')