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
    
    def find_num_node(self, root):
        if root == None:
            return 0  
        return 1 + self.find_num_node(root.left) + self.find_num_node(root.right) 
    
    def ranking(self, data):
        def find_ranking(root, data):
            if not root:
                return 0
            elif data >= root.data:
                return 1 + self.find_num_node(root.left) + find_ranking(root.right, data)
            elif data < root.data:
                return find_ranking(root.left, data)
            
        return find_ranking(self.root, data)
    

T = BST()
inp, data = input('Enter Input : ').split('/')
inp = [int(i) for i in inp.split()]
for i in inp:
    T.insert(i)
T.printTree(T.root)
print('--------------------------------------------------')
print(f'Rank of {data} : {T.ranking(int(data))}')