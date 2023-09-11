class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def insertion(root, data):
            if not root:
                root = Node(data)
            elif root.data > data:
                root.left = insertion (root.left, data)
            elif root.data <= data:
                root.right = insertion(root.right, data)
            return root
        self.root = insertion(self.root, data)
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def findMin(self):
        def find(root):
            if not root.left:
                return root
            return find(root.left)
        return find(self.root)
    
    def findMax(self):
        def find(root):
            if not root.right:
                return root
            return find(root.right)
        return find(self.root)
    
    def findBelow(self, data):
        def find(root, data):
            less_list = []
            if not root:
                return less_list
            elif root.data < data:
                less_list.append(root.data)
            return find(root.left, data) + less_list + find(root.right, data)
        return find(self.root, data)

T = BST()
inp, k = input('Enter Input : ').split('|')
inp = [int(i) for i in inp.split()]
for i in inp:
    T.insert(i)
T.printTree(T.root)
print('--------------------------------------------------')
print(T.findBelow(int(k)))