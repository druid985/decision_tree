#coding=utf-8
'''
@author: WQ
'''
import treepredict
import data
from DecisionTree import DecisionTree

my_data=[['a','USA','yes',18,'None'],
         ['b','France','yes',23,'Premium'],
         ['c','USA','yes',24,'Basic'],
         ['d','France','yes',23,'Basic'],
         ['e','UK','no',18,'Premium'],
         ['f','New Zealand','no',21,'None'],
         ['g','UK','no',12,'Basic'],
         ['h','USA','yes',21,'Premium'],
         ['i','France','no',24,'None'],
         ['j','USA','no',19,'None'],
         ['k','UK','no',18,'None'],
         ['l','UK','yes',18,'None'],
         ['m','New Zealand','yes',19,'None'],
         ['n','UK','yes',12,'Basic'],
         ['o','France','no',18,'Basic'],
         ['p','USA','yes',19,'Basic'],
         ['q','China','no',20,'None'],
         ['r','UK','yes',21,'Basic'],
         ['s','China','no',18,'Premium'],
         ['t','China','no',17,'None'],]

my_data2=[['a','USA','yes','18','None'],
         ['b','France','yes','23','Premium'],
         ['c','USA','yes','24','Basic'],
         ['d','France','yes','23','Basic']]
    

train_flowers = data.read_filedata('..//data//train_data.txt','ALL',',',[0,1,2,3])
test_flowers = data.read_filedata('..//data//test_data.txt','ALL',',',[0,1,2,3])

tree = DecisionTree(train_flowers)
treepredict.buildtree(tree)
tree.printTree()

right = 0
wrong = 0
for flower in test_flowers:
    result = treepredict.predic(tree, flower)
    if flower[-1] in result:
        if right == 49:
            pass
        right += 1
    else:wrong += 1
        
print '正确预测：'+str(right)+'个'
print '错误预测：'+str(wrong)+'个'

print '-------------------------------------------------------------------'

treepredict.prune(tree, 0.95)

tree.printTree()

