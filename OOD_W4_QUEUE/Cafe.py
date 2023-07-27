class Queue:
    def __init__(self, max_size=None):
        self.__items = []
        self.max_size = max_size

    def isEmpty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

    def size(self):
        return len(self.__items)
    
    def isFull(self):
        return self.size() == self.max_size if self.max_size else None
    
    @property
    def items(self):
        return self.__items


class Customer:
    def __init__(self, arrive, coffee_time, customer_id):
        self.arrive = arrive
        self.coffee_time = coffee_time
        self.id = customer_id
        self.wait_time = 0

     
class Cafe:
    def __init__(self, amount_of_barista) -> None:
        self.amount_of_barista = amount_of_barista
        self.customers = Queue()
        self.barista = Queue(self.amount_of_barista)
        self.cafe_queue = Queue()
        
    def add_customers(self, customers):
        customer_id = 1
        for customer in customers:
            self.customers.enqueue(Customer(*customer, customer_id))
            customer_id += 1
            
    def open(self, customers):
        time = 0
        longest_wait = 0
        longest_wait_customer_id = None
        self.add_customers(customers)
        while not self.cafe_queue.isEmpty() or not self.customers.isEmpty() or not self.barista.isEmpty():
            
            while not self.customers.isEmpty() and self.customers.items[0].arrive == time:
                self.cafe_queue.enqueue(self.customers.dequeue())
            
            temp = Queue(self.amount_of_barista)
            while not self.barista.isEmpty():   
                customer = self.barista.dequeue()
                if time - customer.arrive - customer.wait_time == customer.coffee_time:
                    print(f"Time {time} customer {customer.id} get coffee")
                else:
                    temp.enqueue(customer)
            self.barista = temp
            
            while not self.barista.isFull() and not self.cafe_queue.isEmpty():
                customer = self.cafe_queue.dequeue()
                customer.wait_time = time - customer.arrive
                if customer.wait_time > longest_wait:
                    longest_wait = customer.wait_time
                    longest_wait_customer_id = customer.id
                self.barista.enqueue(customer)
                
            time+=1
            
        if longest_wait == 0:
            print("No waiting")
        else:
            print(f"The customer who waited the longest is : {longest_wait_customer_id}")
            print(f"The customer waited for {longest_wait} minutes")
            
            
print(' ***Cafe***')
inputs = input('Log : ')
customers = [[int(x) for x in inp.split(',')] for inp in inputs.split('/')]
cafe = Cafe(2)
cafe.open(customers)