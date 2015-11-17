'''
Created on 2015-11-11

@author: BXD
'''
class Tree:
    
    def __init__(self,id,value,fatherid):
        self.id = id
        self.value = value
        self.fatherid = fatherid
        self.left_children = None
        self.right_children = None
    
    def add_left_child(self,child):
        self.left_children = child
        
    def add_right_child(self,child):
        self.right_children = child
        
    def printTrees(self):
        print self
        
        print '--'*self.id,
        if self.left_children is not None : self.left_children.printTree()
        if self.right_children is not None : self.right_children.printTree()
                
    def __str__(self):
        return str(self.value)

