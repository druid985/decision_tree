'''
Created on 2015-11-11

@author: BXD
'''
class DecisionTree:
    
    def __init__(self,rows=None,id=1):
        self.rows = rows 
        self.id = id
        self.colum = None
        self.colum_value = None
        self.entropy = None
        self.result = None
        self.left_children = None
        self.right_children = None
    
    def printTree(self):
        if self.result is None:
            print self.colum,
            print ':',
            print self.colum_value,
            print '?'
            
            print '    '*self.id,
            print 'T->',
            if self.left_children is None:
                pass
            self.left_children.printTree()
            
            print '    '*self.id,
            print 'F->',
            self.right_children.printTree()
        else : 
            print self.result
            
    def __str__(self):
        return self.printTree()
