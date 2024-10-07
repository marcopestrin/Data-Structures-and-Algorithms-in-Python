class TreeNode:
    # encapsulating data
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def height(self):
        if self is None:
            return 0
        return 1+max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1+TreeNode.size(self.left) + TreeNode.size(self.right)
    
    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + [self.key] +  TreeNode.traverse_in_order(self.right))
    
    def traverse_pre_order(self):
        if self is None:
            return []
        return ([self.key] + TreeNode.traverse_pre_order(self.left) + TreeNode.traverse_pre_order(self.right))

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def display_keys(self, space='\t', level=0):
        if self is None:
            # node is empty
            print(space*level + '-')
            return   
        if self.left is None and self.right is None:
            # node is a leaf
            print(space*level + str(self.key))
            return
        TreeNode.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.left, space, level+1)  
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node