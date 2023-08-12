class Node:
    def __init__(self,data=None):
       self.data = data
       self.next = None
       self.down = None


class SNode:
    def __init__(self, data=None):
        self.data = data
        self.down = None


class Link:
    def __init__(self):
        self.head = Node()

    def next_Node(self,data):
        if self.search(data.data):
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = data
    
    def search(self,data):
        cur_node = self.head
        if cur_node:
            while cur_node.data != data:
                cur_node = cur_node.next
        return cur_node
    
    def next_secondary_Node(self,n,data):
        cur_node = self.search(n)
        if cur_node != self.head:
            while cur_node.down:
                cur_node = cur_node.down
            cur_node.down = data
    
    def show_all(self):
        cur_node = self.head.next
        while cur_node:
            print(f'{cur_node.data} : ', end='')
            cur_down_node = cur_node.down
            while cur_down_node:
                print(f'{cur_down_node.data},', end='')
                cur_down_node = cur_down_node.down
            print()
            cur_node = cur_node.next


inp = input("input : ").split(",")
l = Link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_Node(Node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_Node(h[0],SNode(h[1]))
l.show_all()

#ADN A,ADN B,ADN C,ADN D,ADSN D-A1