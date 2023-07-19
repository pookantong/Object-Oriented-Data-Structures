class Queue:
    def __init__(self) -> None:
        self.__queue = []
        
    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        return self.__queue.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.__queue) == 0

    def size(self):
        return len(self.__queue)
    
    @property
    def queue(self):
        return self.__queue
    
def conceptQueue(inp):
    queue = Queue()
    error_dequeue = 0
    error_inp = 0
    count = 0
    commands = inp.split(',')
    for command in commands:
        print(f'Step : {command}')
        if command[0] == 'D':
            for i in range(int(command[1:])):
                if not queue.dequeue():
                    error_dequeue += 1
            print(f'Dequeue : {queue.queue}')
        elif command[0] == 'E':
            for i in range(int(command[1:])):
                queue.enqueue(f'*{count}')
                count+=1
            print(f'Enqueue : {queue.queue}')
        else:
            error_inp += 1
            print(queue.queue)
        print(f'Error Dequeue : {error_dequeue}')
        print(f'Error input : {error_inp}')
        print('--------------------')
    
inp = input('input : ')
conceptQueue(inp)