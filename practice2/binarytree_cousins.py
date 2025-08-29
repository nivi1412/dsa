#binarytree_cousins.py

#do level order traversal
#store[node,level,parent]
#once level changes take sum of left and right values call a function send (root,left and right ) make a tree
#O(n)

from build_binarytree import build_binarytree,print_binarytree

def binarytree_cousins(root,my_dict,my_list):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.data]
    if root.left is None:
        return [root.right.data]
    if root.right is None:
        return [root.left.data]
    print(root.data)
    left=binarytree_cousins(root.left,my_dict,my_list)
    right=binarytree_cousins(root.right,my_dict,my_list)
    my_dict[root.data] = left + right
    return [root.data]+left+right



bt=input("enter the nodes of the tree: ")
bt=list(bt.split())
my_dict={}
my_list=[]
root=build_binarytree(bt)
binarytree_cousins(root,my_dict,my_list)
print(my_dict)