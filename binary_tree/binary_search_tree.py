from binary_tree import tree, display_keys

# BST (Binary Search Tree) is a binary tree that satisfies the following conditions:
# 1: The left subtree of any node only contains nodes with keys less than the node's key
# 2: The right subtree of any node only contains nodes with keys greater than the node's key

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and  (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    print(node.key, min_key, max_key, is_bst_node)
    return is_bst_node, min_key, max_key

# is_bst(tree) # no BST because 3 is higher than 1

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def insert(node, key, value):
    # Starting from the root node, we compare the key to be inserted with the current node's key
    # If the key is smaller, we recursively insert it in the left subtree (if it exists) or attach it as as the left child if no left subtree exists.
    # If the key is larger, we recursively insert it in the right subtree (if it exists) or attach it as as the right child if no right subtree exists.
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
    
def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

def list_all(node):
    if node is None:
        return []
    # priority on the left side
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

def is_balanced(node):
    # Here's a recursive strategy:
    # Ensure that the left subtree is balanced.
    # Ensure that the right subtree is balanced.
    # Ensure that the difference between heights of left subtree and right subtree is not more than 1.
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    print('balanced_r:',balanced_l,', height_l:',height_l,', balanced_r:',balanced_r,', height_r:',height_r,)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height

# creating nodes
marco = User('marco', 'Marco Pestrin', 'marco_pestrin@example.com')
francesco = User('francesco', 'Francesco Facci', 'francesco_facci@example.com')
gianni = User('gianni', 'Gianni Basso', 'gianni_basso@example.com')
andrea = User('andrea', 'Andrea Chiesa', 'andrea_chiesa@example.com')
martino = User('martino', 'Martino Vanin', 'martino_Vanin@example.com')

# adding user
tree = insert(None, andrea.username, andrea)
insert(tree, gianni.username, gianni)
insert(tree, martino.username, martino)
insert(tree, francesco.username, francesco)
insert(tree, marco.username, marco)
display_keys(tree)

# finding an user
my_node = find(tree, 'marco')
not_found_node = find(tree, 'gilberto')
print('Not found node: ', not_found_node)
print('Found node: ', my_node.value)

# updating an user
update(tree, 'andrea', User('andrea', 'Andrea Campanile', 'andrea_campanile@example.com'))
my_node_updated = find(tree, 'andrea')
print('Edited node: ', my_node_updated.value.name)

# show all nodes
print(list_all(tree))
print(is_balanced(tree))


