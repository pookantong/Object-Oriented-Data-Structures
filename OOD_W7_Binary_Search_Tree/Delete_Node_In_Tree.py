class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
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
    
    def findMinRoot(self, root):
        if not root.left:
            return root.data
        return self.findMinRoot(root.left)
    
    def findNode(self, data):
        def find(root, data):
            if not root:
                return None
            if root.data == data:
                return root
            if data < root.data:
                return find(root.left, data)
            else:
                return find(root.right, data)
        return find(self.root, data)
    
    def delete(self, data):
        status = self.findNode(data)
        def deleteNode(root, data):
            if not root:
                return root
            if data < root.data:
                root.left = deleteNode(root.left, data)
            elif data > root.data:
                root.right = deleteNode(root.right, data)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                root.data = self.findMinRoot(root.right)
                root.right = deleteNode(root.right, root.data)
            return root
        if not status:
            return False
        else:
            self.root = deleteNode(self.root, data)
            return True
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for cmd in data:
    cmd = cmd.split()
    if cmd[0] == 'i':
        tree.insert(int(cmd[1]))
        print(f'insert {cmd[1]}')
        printTree90(tree.root)
    elif cmd[0] == 'd':
        status = tree.delete(int(cmd[1]))
        print(f'delete {cmd[1]}')
        if not status:
            print('Error! Not Found DATA')
        printTree90(tree.root)