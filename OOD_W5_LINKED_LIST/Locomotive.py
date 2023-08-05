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
        temp = self.head
        while temp:
            if temp.next:
                res += str(temp.val) + ' <- '
            else:
                res += str(temp.val)
            temp = temp.next
        return res
        
    def append(self, val):
        new_node = Node(val)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node
            
            
def locomotive_first(linked_list: LinkedList):
    temp = linked_list.head
    while temp.val != '0':
        linked_list.head = temp.next
        linked_list.append(temp.val)
        temp = temp.next  
        

print(' *** Locomotive ***')
inp = input('Enter Input : ').split()
linked_list = LinkedList()
for num in inp:
    linked_list.append(num)
print('Before :', linked_list)
locomotive_first(linked_list)
print('After :', linked_list)
