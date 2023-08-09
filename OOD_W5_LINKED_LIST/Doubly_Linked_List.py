class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def __str__(self):
        string = []
        cur = self.head.next
        for i in range(self.size):
            string.append(cur.val)
            cur = cur.next
        return f'linked list : {"->".join(string)}'
    
    def str_reverse(self):
        reverse_string = []
        cur = self.tail.prev
        for i in range(self.size):
            reverse_string.append(cur.val)
            cur = cur.prev
        return f'reverse : {"->".join(reverse_string)}'
    
    def isEmpty(self):
        return self.size == 0
    
    def append(self, val):
        new_node = Node(val)
        before_tail = self.tail.prev
        new_node.prev = before_tail
        new_node.next = self.tail
        before_tail.next = new_node
        self.tail.prev = new_node
        self.size += 1
        
    def prepend(self, val):
        new_node = Node(val)
        after_head = self.head.next
        new_node.next = after_head
        new_node.prev = self.head
        after_head.prev = new_node
        self.head.next = new_node
        self.size += 1
        
    def insert(self, index, val):
        new_node = Node(val)
        cur = self.head
        if index < 0 or index > self.size:
            return print('Data cannot be added')
        for i in range(index):
            cur = cur.next
        new_node.prev = cur
        new_node.next = cur.next
        cur.next.prev = new_node
        cur.next = new_node
        self.size += 1
        return print(f'index = {index} and data = {val}')
    
    def remove(self, val):
        cur = self.head
        index = 0
        while cur.val != val:
            cur = cur.next
            index+=1
            if index >= self.size:
                return print('Not Found!')
        res = cur
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
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
        linked_list.prepend(val)
    if cmd == "I":
        index, val = val.split(':')
        res = linked_list.insert(int(index), val)
    if cmd == "R":
        linked_list.remove(val)
    print(linked_list)
    print(linked_list.str_reverse())   