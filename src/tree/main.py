'''

@author: WQ
'''

import treepredict
import data
from DecisionTree import DecisionTree

path = '..//data//'
train_file = path + 'weibo_train_data.txt'


train_main = data.read_filedata(train_file,'ALL','|',[5,7,8])

print train_main

#for row in train_main:
#    row.pop(0)
#    row.pop(0)
#    row.pop(1)
#    row.pop(1)
#    row.append(row[0])
#    row.pop(0)

#print train_main
 
#tree = DecisionTree(train_main)
#treepredict.buildtree(tree)
#treepredict.prune(tree, 0.3)
#tree.printTree()


