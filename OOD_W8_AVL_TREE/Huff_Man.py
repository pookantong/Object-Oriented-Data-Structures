class Node:
    def __init__(self, key, freq) -> None:
        self.key = key
        self.freq = freq
        self.left = None
        self.right = None
        self.height = 1
        
    def __str__(self) -> str:
        return str(self.key)
    
def build_tree(encode_node):
    while len(encode_node) != 1:
        least_node1 = encode_node.pop(0)
        least_node2 = encode_node.pop(0)
        new_root = Node('*', least_node1.freq + least_node2.freq)
        new_root.left = least_node1
        new_root.right = least_node2
        new_root.height = max(least_node1.height, least_node2.height) + 1
        encode_node.append(new_root)
        encode_node = sorted(encode_node, key=lambda node: (node.freq, -node.height))
        printTree(new_root)
        print('------------------------------------------------------')
    return encode_node.pop()
    
    
def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)
        
def huffman(root, exp=''):
    if root.key != '*':
        return {root.key: exp}
    return {**huffman(root.right, exp+'1'), **huffman(root.left, exp+'0')}

def encode_string(string, huffman_code):
    huffman_string = ''
    for char in string:
        huffman_string += huffman_code[char]
    return huffman_string
    
            
inp = input('Enter Input : ')
encode_data = {}
for char in inp:
    if char in encode_data:
        encode_data[char] += 1
    else:
        encode_data[char] = 1
print(encode_data) 
encode_node = []
for key, freq in encode_data.items():
    encode_node.append(Node(key, freq))
encode_node = sorted(encode_node, key=lambda node: (node.freq, node.key))
print(*encode_node)
root = build_tree(encode_node)
huffman_code = huffman(root)
print(huffman_code)
printTree(root)
print(f'Encoded! : {encode_string(inp, huffman_code)}')
