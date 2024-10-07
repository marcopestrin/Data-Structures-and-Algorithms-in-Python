class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    
def parse_tuple(data):
    # print("--->", data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree_tuple = ((1,3,None), 2, ((None,3,4), 5, (6,7,8)))
# tuple --> immutability, heterogeneus, nested

tree = parse_tuple(tree_tuple)
# print(tree.key) # 2
# print(tree.left.key) # 3
# print(tree.left.left.key) # 1
# print(tree.left.right) # None
# print(tree.right.key) # 5
# print(tree.right.left.right.left) # None
# print(tree.right.left.right.key) # 4

def display_keys(node, space='\t', level=0):    
    # If the node is empty
    if node is None:
        print(space*level + '-')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level+1) # recursion
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1) # recursion

display_keys(tree, ' ')

def traverse_in_order(node):
    # inorder traversal --> left, current, right --> if there's left leaf skip current
    if node is None:
        return []
    return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

def traverse_pre_order(node):
    # preorder traversal --> current, left, right --> first the current, then subtree on the left and then subtree on the right
    if node is None:
        return []
    return ([node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right))

# Traversing a binary tree:
print('Inorder traverse:', traverse_in_order(tree))
print('Preorder traverse:', traverse_pre_order(tree))

# Height and size of binary tree:
def tree_height(node):
    if node is None:
        return 0
    return max(tree_height(node.left), tree_height(node.right)) +1

def tree_size(node):
    if node is None:
        return 0
    return tree_size(node.left) + tree_size(node.right) +1

print('Tree height:', tree_height(tree), ' Tree size:', tree_size(tree))

