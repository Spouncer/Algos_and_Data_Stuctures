import Tree_funcs_classes as TFC

tree = TFC.RB_Tree('numbers', None)

nodes = [TFC.fem, TFC.elleve, TFC.tolve, TFC.ti, TFC.fire, TFC.to, TFC.en, TFC.nul, TFC.otte, TFC.syv, TFC.tre, TFC.ni, TFC.nifem] #, en, fire , syv, , nul, to, seks, otte, ti, tolve]
      
for node in nodes:
    tree.RB_insert_node(node)
    

for node in nodes:
    print(node.item, node.colour)
    if node.left != None and node.right != None:
        print([node.left.item, node.right.item])
    elif node.left != None:
        print([node.left.item, []])
    elif node.right != None:
        print([[], node.right.item])
    else:
        print([])

print(tree.isRBTree())
print('now delete 9 \n ')


# tree.RB_delete_node(TFC.ni)

# for node in nodes:
#     print(node.item, node.colour)
#     if node.left != None and node.right != None:
#         print([node.left.item, node.right.item])
#     elif node.left != None:
#         print([node.left.item])
#     elif node.right != None:
#         print([node.right.item])
#     else:
#         print([])

# print(tree.isRBTree())

# tree.RB_delete_node(TFC.otte)

# for node in nodes:
#     print(node.item, node.colour)
#     if node.left != None and node.right != None:
#         print([node.left.item, node.right.item])
#     elif node.left != None:
#         print([node.left.item])
#     elif node.right != None:
#         print([node.right.item])
#     else:
#         print([])

# print(tree.isRBTree())

tree.RB_delete_node(TFC.nifem)

for node in nodes:
    print(node.item, node.colour)
    if node.left != None and node.right != None:
        print([node.left.item, node.right.item])
    elif node.left != None:
        print([node.left.item, []])
    elif node.right != None:
        print([[], node.right.item])
    else:
        print([])

print(tree.isRBTree())