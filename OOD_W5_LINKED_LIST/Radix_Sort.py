class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None
        self.prev = None    
    

class DoublyLinkedList:
    def __init__(self) -> None:
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.size = 0
        
    def __str__(self):
        string = []
        temp = self.dummy.next
        for i in range(self.size):
            string.append(temp.val)
            temp = temp.next
        return f'linked list : {" -> ".join(string)}'
    
    def str_reverse(self):
        reverse_string = []
        temp = self.dummy.prev
        for i in range(self.size):
            reverse_string.append(temp.val)
            temp = temp.prev
        return f'reverse : {"->".join(reverse_string)}'
    
    def isEmpty(self):
        return self.size == 0
    
    def append(self, val):
        new_node = Node(val)
        new_node.prev = self.dummy.prev
        new_node.next = self.dummy
        self.dummy.prev.next = new_node
        self.dummy.prev = new_node
        self.size += 1
        
    def add_before(self, val):
        new_node = Node(val)
        new_node.next = self.dummy.next
        new_node.prev = self.dummy
        self.dummy.next.prev = new_node
        self.dummy.next = new_node
        self.size += 1
        
    def insert(self, index, val):
        new_node = Node(val)
        temp = self.dummy
        if index < 0 or index > self.size:
            return print('Data cannot be added')
        for i in range(index):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        self.size += 1
        return print(f'index = {index} and data = {val}')
    
    def remove_head(self):
        res = self.dummy.next
        self.dummy.next = self.dummy.next.next
        self.dummy.next.prev = self.dummy
        return res
    
def radix_sort(linked_list):
    max_val = get_max_val(linked_list)
    
    if not max_val:
        return
    
    exp = 1 # Exponential
    while max_val//exp > 0:
        linked_list_sort(linked_list, exp)
        exp *= 10
            
def get_max_val(linked_list):
    max_val = None
    temp = linked_list.dummy.next
    while temp.val:
        max_val = max(temp.val, max_val)
        temp = temp.next
    return max_val

def linked_list_sort(linked_list, exp):
    linked_list.dummy.prev = None
    current_node = linked_list.dummy.next
    for i in range(linked_list.size()):
        next_node = current_node.next
        
        if current_node.val%exp or not linked_list.dummy.prev:
            pass
        
        
    
    
