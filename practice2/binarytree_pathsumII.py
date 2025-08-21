#binarytree_pathsumII.py

from build_binarytree import build_binarytree,print_binarytree


tree=input("enter the nodes of the tree: ")
tree=list(tree.split())
psum=int(input("enter the sum: "))
root=build_binarytree(tree)
pathsum(root,psum)