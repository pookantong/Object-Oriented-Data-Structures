class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        # Init Circular Linked List 
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        #Init Linked List
        self.head = self.dummy
        self.tail = self.dummy
        self.size = 0
        
    def __str__(self):
        string = []
        temp = self.head
        for i in range(self.size):
            string.append(temp.val)
            temp = temp.next
        return f'linked list : {"->".join(string)}'
    
    def str_reverse(self):
        reverse_string = []
        temp = self.tail
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
        self.head = self.dummy.next
        self.tail = self.dummy.prev
        self.size += 1
        
    def add_before(self, val):
        new_node = Node(val)
        new_node.next = self.dummy.next
        new_node.prev = self.dummy
        self.dummy.next.prev = new_node
        self.dummy.next = new_node
        self.head = self.dummy.next
        self.tail = self.dummy.prev
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
        self.head = self.dummy.next
        self.tail = self.dummy.prev
        self.size += 1
        return print(f'index = {index} and data = {val}')
    
    def remove(self, val):
        temp = self.dummy.next
        index = 0
        while temp.val != val:
            temp = temp.next
            index+=1
            if index >= self.size:
                return print('Not Found!')
        res = temp
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.head = self.dummy.next
        self.tail = self.dummy.prev
        self.size -= 1
        print(f'removed : {val} from index : {index}')
        return res
    
    
inp = input('Enter Input : ').split(',')
linked_list = DoublyLinkedList()
for cmds in inp:
    cmd, val = cmds.split()
    if cmd == "A":
        linked_list.append(val)
    if cmd == "Ab":
        linked_list.add_before(val)
    if cmd == "I":
        index, val = val.split(':')
        res = linked_list.insert(int(index), val)
    if cmd == "R":
        linked_list.remove(val)
    print(linked_list)
    print(linked_list.str_reverse())   
    
# size = 0 | Dummy <=> Dummy
# size = 1 | Dummy <=> Head,Tail <=> Dummy
# size = 2 | Dummy <=> Head <=> Tail <=> Dummy
# Use Dummy In Main Algorithm To Process Only