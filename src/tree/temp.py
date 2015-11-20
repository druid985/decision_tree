#coding=utf-8
'''
@author: WQ
'''
import treepredict
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
    
def clean_data(file_data):
    return_list = []
    for s in file_data:
        temp_list = s.split(',')
        temp_list[0] = float(temp_list[0])
        temp_list[1] = float(temp_list[1])
        temp_list[2] = float(temp_list[2])
        temp_list[3] = float(temp_list[3])
        temp_list[-1] = temp_list[-1].replace('\n','')
        return_list.append(temp_list)
    return return_list

file = open('../data/test_data.txt','r')
try:
    file_data = file.readlines()
finally:
    file.close()
    
my_data4 = clean_data(file_data)

file = open('../data/train_data.txt','r')
try:
    file_data = file.readlines()
finally:
    file.close()

my_data3 = clean_data(file_data)

#treepredict.decisionTree.rows = my_data3
#treepredict.buildtree()
#treepredict.decisionTree.printTree()

tree = DecisionTree(my_data3)
treepredict.buildtree(tree)
tree.printTree()

right = 0
wrong = 0
for data in my_data4:
    if data[-1]==treepredict.predic(tree, data):
        right += 1
    else:wrong += 1
        
print '正确预测：'+str(right)+'个'
print '错误预测：'+str(wrong)+'个'

print '-------------------------------------------------------------------'

treepredict.prune(tree, 0.95)

tree.printTree()

#print treepredict.entropy([[1],[1],[2],[2],[2],[3],[3],[4],[4],[4],[4]])
#print treepredict.entropy([[1],[1],[2],[2],[2]])
#print treepredict.entropy([[3],[3],[4],[4],[4],[4]])
