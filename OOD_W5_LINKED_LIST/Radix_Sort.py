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
        
    def __str__(self) -> str:
        string = []
        cur = self.head.next
        for i in range(self.size):
            string.append(cur.val)
            cur = cur.next
        return " -> ".join([str(x) for x in string])
    
    def to_str(self) -> str:
        string = ""
        cur = self.head.next
        while cur.val != None:
            string += str(cur.val) + ' '
            cur = cur.next
        return string
        
    def append(self, val):
        new_node = Node(val)
        before_tail = self.tail.prev
        new_node.prev = before_tail
        new_node.next = self.tail
        before_tail.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def pop_left(self):
        res = self.head.next
        if res == self.tail:
            return None
        else:
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            self.size -= 1
            return res
        
    def prepend(self, val):
        new_node = Node(val)
        after_head = self.head.next
        new_node.next = after_head
        new_node.prev = self.head
        after_head.prev = new_node
        self.head.next = new_node
        self.size += 1

    def pop(self):
        res = self.tail.prev
        if res == self.head:
            return None
        else:
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.size -= 1
            return res
    
    def isEmpty(self):
        return self.size == 0
        
        
def get_max_digit(nums):
    max_num = float('-inf')
    for num in nums:
        max_num = max(max_num, abs(num))
    
    return len(str(max_num))

def get_digit(num, digit):
    num = abs(num)
    for i in range(digit-1):
        num //= 10
    return num%10

def radix_sort(nums):
    print('------------------------------------------------------------')
    sort_num = sorted(nums)
    max_digit = get_max_digit(nums)
    before_linked_list = DoublyLinkedList()
    linked_list = DoublyLinkedList()
    check_linked_list = DoublyLinkedList()
    for num in nums:
        linked_list.append(num)
        before_linked_list.append(num)
    if sort_num == nums:
        print(f'0 Time(s)')
        print(f'Before Radix Sort : {before_linked_list}')
        print(f'After  Radix Sort : {linked_list}')
        return
    pos_digits = [DoublyLinkedList() for i in range(10)]
    neg_digits = [DoublyLinkedList() for i in range(10)]

    for cur_digit in range(1, max_digit+1):
        print(f'Round : {cur_digit}')
        while not linked_list.isEmpty():
            cur_node = linked_list.pop_left()
            cur_num = cur_node.val  
            num_digit = get_digit(cur_num, cur_digit)
            pos_digits[num_digit].append(cur_num) if cur_num >= 0 else neg_digits[num_digit].append(cur_num)
        for i in range(10):
            print(f'{i} : {pos_digits[i].to_str()}{neg_digits[i].to_str()}')
            while not pos_digits[i].isEmpty():
                linked_list.prepend(pos_digits[i].pop().val)
            while not neg_digits[i].isEmpty():
                linked_list.append(neg_digits[i].pop_left().val)
        print('------------------------------------------------------------')

    print(f'{max_digit} Time(s)')
    print(f'Before Radix Sort : {before_linked_list}')
    print(f'After  Radix Sort : {linked_list}')



nums = [int(x) for x in input('Enter Input : ').split()]
radix_sort(nums)

    
    
