from binary_tree import tree, display_keys
from User import User

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    # BST (Binary Search Tree) is a binary tree that satisfies the following conditions:
    # 1: The left subtree of any node only contains nodes with keys less than the node's key
    # 2: The right subtree of any node only contains nodes with keys greater than the node's key
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and  (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    print(node.key, min_key, max_key, is_bst_node)
    return is_bst_node, min_key, max_key

def insert(node, key, value):
    # Starting from the root node, we compare the key to be inserted with the current node's key
    # If the key is smaller, we recursively insert it in the left subtree (if it exists) or attach it as as the left child if no left subtree exists.
    # If the key is larger, we recursively insert it in the right subtree (if it exists) or attach it as as the right child if no right subtree exists.
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        # in alphabetical order this name is before the key name --> add to left side
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        # in alphabetical order this name is after the key name --> add to right side
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
    # The tree is balanced i.e. it does not skew too heavily to one side or the other.
    # The left and right subtrees of any node shouldn't differ in height/depth by more than 1 level.
    # Here's a recursive strategy:
    # Ensure that the left subtree is balanced.
    # Ensure that the right subtree is balanced.
    # Ensure that the difference between heights of left subtree and right subtree is not more than 1.
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    # print('balanced_r:',balanced_l,', height_l:',height_l,', balanced_r:',balanced_r,', height_r:',height_r,)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height

def make_balanced_bst(data, lo=0, hi=None, parent=None):
    #  create a balanced BST from a sorted list/array of key-value pairs
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    key, value = data[mid]
    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    return root

def balance_bst(node):
    return make_balanced_bst(list_all(node))

# is_bst(tree) # no BST because 3 is higher than 1

# creating nodes
andrea = User('Andrea', 'Andrea Chiesa', 'andrea_chiesa@example.com')
giacomino = User('Giacomino', 'Giacomino Rossi', 'giacomino_rossi@example.com')
gabriele = User('Gabriele', 'Gabriele Franchetto', 'gabriele_franchetto@example.com')
giacomo = User('Giacomo', 'Giacomo Bagolato', 'giacomo_bagolato@example.com')
gianni = User('Gianni', 'Gianni Basso', 'gianni_basso@example.com')
leonardo = User('Leonardo', 'Leonardo Bosco', 'leonardo_bosco@example.com')
martino = User('Martino', 'Martino Pestrin', 'martino_pestrin@example.com')
francesco = User('Francesco', 'Francesco Cortese', 'francesco_cortese@example.com')
marco = User('Marco', 'Marco Facci', 'marco_facci@example.com')
gianluca = User('Gianluca', 'Gianluca Guba', 'gianluca_guba@example.com')

print('--------------------------------------')
print('### Simple adding users (nodes into a tree)')
tree = insert(None, andrea.username, andrea)
# insert(tree, gianni.username, gianni)
# insert(tree, martino.username, martino)
# insert(tree, francesco.username, francesco)
insert(tree, marco.username, marco)
display_keys(tree)

print('--------------------------------------')
print('### Finding User:')
my_node = find(tree, 'Marco')
not_found_node = find(tree, 'gilberto')
print('Not found node: ', not_found_node)
print('Found node: ', my_node.value)

print('--------------------------------------')
print('### Updating User:')
update(tree, 'andrea', User('Andrea', 'Andrea Campanile', 'andrea_campanile@example.com'))
my_node_updated = find(tree, 'Andrea')
print('Edited node: ', my_node_updated.value.name)

print('--------------------------------------')
print('### Show all nodes')
print(list_all(tree))
print(is_balanced(tree))

print('--------------------------------------')
print('### Creating manually a balanced tree:')
tree2 = insert(None, giacomo.username, giacomo) # tree root

insert(tree2, gabriele.username, gabriele)
# Gabriele is left than Giacomo because A (gAbriele) is before I (gIacomo)

insert(tree2, gianni.username, gianni)
# Gianni is right than Giacomo because N (giaNni) is after C (giaComo)

insert(tree2, leonardo.username, leonardo)
# Leonardo is right than Giacomo because L (Leonardo) is after G (Giacomo)
# Leonardo is right than Gianni because L (Leonardo) is after G (Gianni)

insert(tree2, andrea.username, andrea)
# Andrea is left than Giacomo because A (Andrea) is before G (Giacomo)
# Andrea is left than Gabriele because A (Andrea) is before G (Gabriele)

#                 Leonardo
#         Gianni
#                 -
# Giacomo
#                 -
#         Gabriele
#                 Andrea

insert(tree2, gianluca.username, gianluca)
# Gianluca is after Giacomo (go right) and before Gianni (go left)

insert(tree2, giacomino.username, giacomino)
# Giacomino is before Giacomo (go left) and after Gabriele (go right)

#                 Leonardo
#         Gianni
#                 Gianluca
# Giacomo
#                 Giacomino
#         Gabriele
#                 Andrea


display_keys(tree2)
print('Is Balanced? ', is_balanced(tree))

print('--------------------------------------')
print('### Create automatically a balanced tree:')
users = [andrea, giacomino, gabriele, giacomo, gianni, leonardo, martino, francesco, marco, gianluca]
data = [(user.username, user) for user in users]
balanced_data = make_balanced_bst(data)
display_keys(balanced_data)

print('--------------------------------------')
print('### Creating unbalanced tree:')
tree3 = None
for user in users:
    tree3 = insert(tree3, user.username, user)
display_keys(tree3)
print('Is Balanced? ', is_balanced(tree3))

print('--------------------------------------')
print('### Balance unbalanced tree:')
tree4 = balance_bst(tree3)
display_keys(tree4)
print('Is Balanced? ', is_balanced(tree4))


