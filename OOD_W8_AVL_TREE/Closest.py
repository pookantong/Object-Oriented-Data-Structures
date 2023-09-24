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
    
    def find_closest(self, data):
        def find(root, data, closest=root.data):
            if not root:
                return closest
            elif data == root.data:
                return root.data
            elif abs(data-root.data) < abs(data-closest):
                closest = root.data
            left = find(root.left, data, closest)
            right = find(root.right, data, closest)
            if abs(data-left) < abs(data-right):
                return left
            return right
        return find(self.root, data)
            
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp, k = input('Enter Input : ').split('/')
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
    T.printTree(root)
    print('--------------------------------------------------')
print(f'Closest value of {k} : {T.find_closest(int(k))}')