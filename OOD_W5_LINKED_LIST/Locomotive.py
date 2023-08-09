class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        
    def __str__(self) -> str:
        res = ''
        cur = self.head
        while cur:
            if cur.next:
                res += str(cur.val) + ' <- '
            else:
                res += str(cur.val)
            cur = cur.next
        return res
        
    def append(self, val):
        new_node = Node(val)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node
            
            
def locomotive_first(linked_list: LinkedList):
    cur = linked_list.head
    while cur.val != '0':
        linked_list.head = cur.next
        linked_list.append(cur.val)
        cur = cur.next  
        

print(' *** Locomotive ***')
inp = input('Enter Input : ').split()
linked_list = LinkedList()
for num in inp:
    linked_list.append(num)
print('Before :', linked_list)
locomotive_first(linked_list)
print('After :', linked_list)
