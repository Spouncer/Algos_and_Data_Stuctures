import Tree_funcs_classes as TFC

# for i in range(7, 10):
#     print(tree.binary_search(i))


# def BFS_search(tree, value, d):
#     node = tree.root
#     found = 0
    
#     if node != None and d == 0:
#         if value == node.item:
#             print(f'The node {value} is the root of the tree.')
#             found += 1

#     if found == 0:       
#         if node.left != None:
#             print(node.left.item)
#             if value == node.left.item:
#                 found += 1
#                 print(f'The node {value} is in the tree at depth {d+1}.')

#         if node.right != None: 
#             print(node.right.item)
#             if value == node.right.item:
#                 found += 1
#                 print(f'The node {value} is in the tree at depth {d+1}.')

#     return found

i = 8
print('DFS Search')
print(TFC.tree.DFS_search(i))

print('BFS Search')
print(TFC.tree.BFS_Search(i, 0))




