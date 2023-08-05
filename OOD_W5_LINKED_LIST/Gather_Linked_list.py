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
        self.head = self.dummy
        self.tail = self.dummy
        
        
    def __str__(self) -> str:
        res = ''
        temp = self.head
        while temp.next.val:
            res += f'{temp.val} '
            temp = temp.next
        res += str(temp.val)
        return res
        
    def __add__(self, linked_list_2):
        temp_2 = linked_list_2.tail
        while temp_2.val:
            temp_2 = temp_2.prev
            self.append(temp_2.next.val)
        return self  
        
    def append(self, val):
        new_node = Node(val)
        new_node.prev = self.dummy.prev
        new_node.next = self.dummy
        self.dummy.prev.next = new_node
        self.dummy.prev = new_node
        self.head = self.dummy.next
        self.tail = self.dummy.prev


def add_list_val_to_ll(linked_list, list_val):
    for val in list_val:
        linked_list.append(val)


inp_1, inp_2 = input('Enter Input (L1,L2) : ').split()
inp_1 = inp_1.split('->')
inp_2 = inp_2.split('->')
linked_list_1 = DoublyLinkedList()
linked_list_2 = DoublyLinkedList()
add_list_val_to_ll(linked_list_1, inp_1)
add_list_val_to_ll(linked_list_2, inp_2)
print('L1    :', *inp_1)
print('L2    :', *inp_2)
print('Merge :', linked_list_1+linked_list_2)
