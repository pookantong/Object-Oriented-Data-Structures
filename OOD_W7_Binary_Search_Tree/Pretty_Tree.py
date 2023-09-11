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
    
    def __str__(self) -> str:
        lines = BST._build_tree_string(self.root, 0, False, "-")[0]
        return "\n".join((line.rstrip() for line in lines))
    
    def _build_tree_string( 
        root: Node,
        curr_index: int,
        include_index: bool = False,
        delimiter: str = "-") :
        if root is None:
            return [], 0, 0, 0
        line1 = []
        line2 = []
        if include_index:
            node_repr = "{}{}{}".format(curr_index, delimiter, root.data)
        else:
            node_repr = str(root.data)
        new_root_width = gap_size = len(node_repr)
        l_box, l_box_width, l_root_start, l_root_end = \
            BST._build_tree_string(root.left, 2 * curr_index + 1, include_index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            BST._build_tree_string(root.right, 2 * curr_index + 2, include_index, delimiter)
        if l_box_width > 0:
            l_root = l_box_width - l_root_end - 1
            line1.append(" " * (l_box_width + 1))
            line2.append(" " * (l_box_width - l_root))
            line2.append("_" * l_root + "/")
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0
        line1.append(node_repr)
        line2.append(" " * new_root_width)
        if r_box_width > 0:
            line1.append(" " * (r_box_width + 1))
            line2.append("\\" + "_" * (r_root_start))
            line2.append(" " * r_box_width)
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1
        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)
        return new_box, len(new_box[0]), new_root_start, new_root_end

T = BST()
inp = [int(i) for i in input('Enter input: ').split()]
for i in inp:
    T.insert(i)
print(T)