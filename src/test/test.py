import Tree
'''
Created on 2015-11-9

@author: BXD
'''
data = [1,2,3,4,5,6,7,8,9,10]
tree1 = Tree.Tree(1,data,0)

def build_tree(tree):
    
    if len(tree.value)<=1 : return
    
    row_len = len(tree.value)
    left_tree = Tree.Tree(tree.id+1,tree.value[0:row_len/2],tree.id)
    right_tree = Tree.Tree(tree.id+1,tree.value[row_len/2:],tree.id)
    tree.add_left_child(left_tree)
    tree.add_right_child(right_tree)
    
    build_tree(left_tree)
    build_tree(right_tree)

build_tree(tree1)

tree1.printTrees()

