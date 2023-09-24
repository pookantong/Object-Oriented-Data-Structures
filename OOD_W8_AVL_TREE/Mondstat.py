class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.height = 0
        self.num = 0

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.num += 1
        else:
            h = height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root
            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num+=1
            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num+=1
            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)
                else:
                    insert_subtree(current.right,self.num - pow(2,h),val)
                self.num+=1
                
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
    
    def compare_power(self, team1, team2):
        order1 = []
        order2 = []
        while team1 != 0:
            if team1%2 == 0:
                team1-=2
                team1/=2
                order1.append('r')
            else:
                team1-=1
                team1/=2
                order1.append('l')
        while team2 != 0:
            if team2%2 == 0:
                team2-=2
                team2/=2
                order2.append('r')
            else:
                team2-=1
                team2/=2
                order2.append('l')
        root1 = self.root
        root2 = self.root
        while order1 != []:
            if order1.pop() == 'l':
                root1 = root1.left
            else:
                root1 = root1.right
        while order2 != []:
            if order2.pop() == 'l':
                root2 = root2.left
            else:
                root2 = root2.right
        power_team1 = gather_power(root1)
        power_team2 = gather_power(root2)
        if power_team1 > power_team2:
            return '>'
        elif power_team1 == power_team2:
            return '='
        else:
            return '<'
                
        
                    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def gather_power(root):
    if root == None:
        return 0
    return root.data + gather_power(root.right) + gather_power(root.left)
            
def insert_subtree( r,num,val):
    if r != None:
        h = height(r)
        max_node = pow(2,h+1)-1
        current = r
        if num+1 > max_node:
            while(current.left != None):
                current = current.left
            current.left = Node(val)
            return
        elif num+1 == max_node:
            while(current.right != None):
                current = current.right
            current.right = Node(val)
            return
        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
            insert_subtree(current.left,num - round(pow(2,h)/2),val)
        else:
            insert_subtree(current.right,num - pow(2,h),val)
    else:
        return

def height(root):
    if root == None:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        if left>right:
            return left + 1
        else:
            return right + 1

T = BST()
power_list, group = input('Enter Input : ').split('/')
power_list = [int(i) for i in power_list.split()]
for i in power_list:
    root = T.insert(i)
print(gather_power(T.root))
for i in group.split(','):
    team1, team2 = i.split()
    print(f'{team1}{T.compare_power(int(team1), int(team2))}{team2}')
