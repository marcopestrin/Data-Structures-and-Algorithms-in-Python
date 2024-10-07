from TreeNode import TreeNode

tree_tuple = ((1,3,18), 2, ((15,3,4), 16, (6,7,(None,3, 1))))

tree = TreeNode.parse_tuple(tree_tuple)
print(tree)
print('_______________')
print(tree.display_keys('  '))
print('_______________')
print('Height: ',tree.height())
print('Size: ',tree.size())
print('Inorder traverse: ',tree.traverse_in_order())
print('Preorder traverse: ',tree.traverse_pre_order())
print('Tuple: ',tree.to_tuple())
