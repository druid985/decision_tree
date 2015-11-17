#coding=utf-8
import DecisionTree
from math import log
'''
@author: WQ
'''

decisionTree = DecisionTree.DecisionTree()

def compare_row(row,colum,value):
    compare_function=None
    if isinstance(value, int) or isinstance(value, float):
        compare_function = lambda row:row[colum]>=value
    else:
        compare_function = lambda row:row[colum]==value
        
    return compare_function(row)

def divideset(rows,colum,value):
    
    list1 = [row for row in rows if compare_row(row,colum,value)]
    list2 = [row for row in rows if not compare_row(row,colum,value)]
    
    return (list1,list2)

def uniqueconts(rows):
    result={}
    for row in rows:
        r = row[-1]
        if r not in result:result[r]=0
        result[r] +=1
    return result

#这是基尼系数的标准公式
def giniimpurity(rows):
    total = len(rows)
    count = uniqueconts(rows)
    imp = 0
    for i in count: 
        p = float(count[i])/total
        imp+=p**2
    return 1-imp 

def entropy(rows):
    total = len(rows)
    count = uniqueconts(rows)
    ent = 0.0
    for i in count: 
        p = float(count[i])/total
        ent-=p*log(p,2)
    return ent
    
def buildtree(tree=None,scoref=entropy):
    if tree is None : tree = decisionTree
    
    rows = tree.rows
    base_score = scoref(rows)
    base_colum_count = len(rows[0])
    
    if base_score == 0:
        tree.result = uniqueconts(rows)
        return

    best_gain = 0    
    best_colum = None
    best_colum_value = None
    best_lists = None

    for colum_index in range(base_colum_count-1):
        for row in rows:
            set1,set2 = divideset(rows, colum_index, row[colum_index])
            gain = base_score-float(len(set1))/len(rows)*scoref(set1)-float(len(set2))/len(rows)*scoref(set2)
            if gain > best_gain:
                best_gain = gain
                best_colum = colum_index
                best_colum_value = row[colum_index]
                best_lists = (set1,set2)
                
    if best_gain>0:
        left_tree = DecisionTree.DecisionTree(rows=best_lists[0],id=tree.id+1)
        right_tree = DecisionTree.DecisionTree(rows=best_lists[1],id=tree.id+1)
        
        tree.colum = best_colum
        tree.colum_value = best_colum_value
        tree.entropy = base_score
        tree.left_children = left_tree
        tree.right_children = right_tree
        
        buildtree(left_tree)
        buildtree(right_tree)    
    
def predic(tree,row):
    if tree.result is None:
        if compare_row(row, tree.colum, tree.colum_value):
            return predic(tree.left_children,row)
        else :
            return predic(tree.right_children,row)
    else:
        return tree.result.keys()[0]
    
