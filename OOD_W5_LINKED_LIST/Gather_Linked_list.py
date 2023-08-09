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
        
        
    def __str__(self) -> str:
        res = ''
        cur = self.head.next
        while cur != self.tail:
            res += f'{cur.val} '
            cur = cur.next
        return res
        
    def __add__(self, linked_list_2):
        cur_2 = linked_list_2.tail.prev
        while cur_2 != linked_list_2.head:
            self.append(cur_2.val)
            cur_2 = cur_2.prev
        return self
        
    def append(self, val):
        new_node = Node(val)
        before_tail = self.tail.prev
        new_node.prev = before_tail
        new_node.next = self.tail
        before_tail.next = new_node
        self.tail.prev = new_node


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