# Normal Queue
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

# Queue That Link To Next Queue
class LinkQueueForLongWait:
    def __init__(self, charge_time, max_size) -> None:
        self.__queue = []
        self.__charge_time = charge_time
        self.__max_size = max_size
        self.__time = 0
        # For Init Next Queue
        self.next = None
       
    # If Queue Is Full Enqueue To Next Queue   
    def enqueue(self, item):
        if not self.full():
            self.__queue.append(item)
        else:
            self.next.enqueue(item)

    def dequeue(self):
        return self.__queue.pop(0) if not self.isEmpty() else -1

    def isEmpty(self):
        return len(self.__queue) == 0

    def size(self):
        return len(self.__queue)
    
    def full(self):
        return self.size() == self.__max_size if self.__max_size != None else None
    
    # Update Time If Have Queue
    def update_time(self):
        if not self.isEmpty():
            self.__time += 1
        else: 
            self.__time = 0
        return self.__time
    
    # Dequeue If Charge Time Is Finish
    def complete_charge(self):
        if not self.isEmpty() and self.__time%self.__charge_time == 0:
            self.dequeue()
    
    @property
    def queue(self):
        return self.__queue
    
    @property
    def max_size(self):
        return self.__max_size
    
    @property
    def time(self):
        return self.__time
    
class LongWait:
    def __init__(self) -> None:
        self.row_1 = Queue()
        self.cashier_1 = LinkQueueForLongWait(3, 5)
        self.cashier_2 = LinkQueueForLongWait(2, 5)
        # Init Link Queue
        self.cashier_1.next = self.cashier_2
        
    def start(self, inp):
        # Enqueue All Of Char To Row 1
        for char in inp:
            self.row_1.enqueue(char)
        while not self.row_1.isEmpty():
            # Auto Enqueue To Cashier 2 If Cashier 1 Is Full
            self.cashier_1.enqueue(self.row_1.dequeue())
            self.cashier_1.update_time()
            self.cashier_2.update_time()
            print(self.cashier_1.time, self.row_1.queue, self.cashier_1.queue, self.cashier_2.queue)
            self.cashier_1.complete_charge()
            self.cashier_2.complete_charge()
                
long_wait = LongWait()
inp = input('Enter people : ')
long_wait.start(inp)