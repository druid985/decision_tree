'''
Created on 2015-11-12

@author: BXD
'''

#这是基尼系数《集体编程智慧》中的公式，有巧妙的避开了平方
def giniimpurity(rows):
    total = len(rows)
    count = uniqueconts(rows)
    imp = 0
    for k in count:
        p1 = float(count[k])/total
        for j in count:
            if k==j : continue
            p2 = float(count[j])/total
            imp+=p1*p2
    return imp

def buildtree(rows,scoref=entropy):
    base_score = scoref(rows)
    base_colum_count = len(rows[0])

    best_gain = 0    
    best_colum = None
    best_value = None
    best_lists = None

    for colum_index in range(base_colum_count-1):
        for row in rows:
            set1,set2 = divideset(rows, colum_index, row[colum_index])
            gain = base_score-float(len(set1))/len(rows)*scoref(set1)-float(len(set2))/len(rows)*scoref(set2)
            if gain > best_gain:
                best_gain = gain
                best_colum = colum_index
                best_value = row[colum_index]
                best_lists = (set1,set2)
                
    if best_gain>0:
        decisionnode(best_colum,best_value,best_lists[0],best_lists[1])
        buildtree(best_lists[0])
        buildtree(best_lists[1])
    else:
        return decisionnode(result = uniqueconts(rows))
    
def decisionnode(colum=None,colum_value=None,left_children=None,right_children=None,result=None):
    if colum is not None and colum_value is not None :
        decisionTree.colum = colum
        decisionTree.colum_value = colum_value
        decisionTree.left_children = left_children
        decisionTree.right_children = right_children
        
    if result is not None:
        decisionTree.result = result
    
#这颗造树函数有误，但由于是我第一次思考做出来的，故留作纪念
def buildtree_problem(rows,scoref=entropy):
    base_score = scoref(rows)

    best_gain = 0    
    best_colum = None
    best_value = None
    best_list1 = []
    best_list2 = []
    items = {}
    
    #本想在此循环取出所有的item，当作字典的key，列索引当作value，但是发现如此循环，不同列有相同数值的时候，会产生bug
    for row in rows:
        for index,item in enumerate(row[0:-1]):
            items[item]=index
    
    for item in items:
        set1,set2 = divideset(rows, items[item], item)
        gain = base_score-float(len(set1))/len(rows)*scoref(set1)-float(len(set2))/len(rows)*scoref(set2)
        if gain >= best_gain:
            best_gain = gain
            best_colum = items[item]
            best_value = item
            best_list1 = set1
            best_list2 = set2
            
    print 'colum:'+best_colum,'value:'+best_value,'entropy:'+best_gain
    print best_list1
    print best_list2
    return best_list1,best_list2
            
#print entropy([['g', 'UK', 'no', '12', 'Basic'], ['n', 'UK', 'yes', '12', 'Basic']])
