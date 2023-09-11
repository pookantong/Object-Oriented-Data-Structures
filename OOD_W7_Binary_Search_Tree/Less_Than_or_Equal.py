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
    
    def findLessOrEqual(self, data):
        def find(root, data):
            count = 0
            if not root:
                return 0
            elif root.data <= data:
                count += 1
            return count + find(root.left, data) + find(root.right, data)
        return find(self.root, data)

T = BST()
inp, k = input('Enter Input : ').split('/')
inp = [int(i) for i in inp.split()]
for i in inp:
    T.insert(i)
T.printTree(T.root)
print('--------------------------------------------------')
print(T.findLessOrEqual(int(k)))