#coding=UTF-8
from tools.tool import print_new
from math import sqrt

critics1={'李楠':{'一代宗师':'2.5','小时代':'3.5','钢铁侠':'2.0','蜘蛛侠':'3.5','重返地球':'2.5','007':'3.0'},
         '宋瑶':{'一代宗师':'1.0','小时代':'3.5','超人':'1.0','蜘蛛侠':'2.5','星际穿越':'2.5','007':'2.0'},
         '吴琼':{'一代宗师':'1.5','小时代':'2.5','钢铁侠':'3.0','蝙蝠侠':'2.5','星际穿越':'1.5','007':'1.0'},
         '卞雪达':{'一代宗师':'2.0','小时代':'1.5','钢铁侠':'3.0','蜘蛛侠':'2.5','星际穿越':'1.5','007':'4.0','生化危机':'5.0'},
         '卞冬至':{'一代宗师':'2.5','小时代':'4.0','超人':'3.0','蜘蛛侠':'1.5','星际穿越':'1.5','007':'3.0'},
         '吴会来':{'一代宗师':'3.0','小时代':'1.0','钢铁侠':'3.5','蜘蛛侠':'4.0','星际穿越':'4.0','007':'2.0'},
         '张薇':{'一代宗师':'4.0','小时代':'1.0','超人':'3.5','蜘蛛侠':'2.0','星际穿越':'3.0','007':'3.5','生化危机':'4.0'},
         '尼培伦':{'一代宗师':'3.5','小时代':'2.5','钢铁侠':'4.0','蜘蛛侠':'3.0','重返地球':'2.0','007':'2.5'},
         '石相扬':{'一代宗师':'4.5','小时代':'0.5','钢铁侠':'4.5','蜘蛛侠':'3.5','星际穿越':'2.5','007':'1.5'},
         '王瑞元':{'一代宗师':'0.5','小时代':'4.5','超人':'1.0','蝙蝠侠':'3.5','星际穿越':'3.0','007':'3.0'},
         '大宝':{'我爱你':'0.5','小时代3':'4.5','超人2':'1.0','蝙蝠侠2':'3.5'}}

critics2={'A':{'The Master':'2.5','Little Time':'3.5','Iron Man':'2.0','Spade Man':'3.5','Return Earth':'2.5','007':'3.0'},
         'B':{'The Master':'1.0','Little Time':'3.5','Super Man':'1.0','Spade Man':'2.5','Interstellar':'2.5','007':'2.0'},
         'C':{'The Master':'1.5','Little Time':'2.5','Iron Man':'3.0','Batman':'2.5','Interstellar':'1.5','007':'1.0'},
         'D':{'The Master':'2.0','Little Time':'1.5','Iron Man':'3.0','Spade Man':'2.5','Interstellar':'1.5','007':'4.0','Resident Evil':'5.0'},
         'E':{'The Master':'2.5','Little Time':'4.0','Super Man':'3.0','Spade Man':'1.5','Interstellar':'1.5','007':'3.0'},
         'F':{'The Master':'3.0','Little Time':'1.0','Iron Man':'3.5','Spade Man':'4.0','Interstellar':'4.0','007':'2.0'},
         'H':{'The Master':'4.0','Little Time':'1.0','Super Man':'3.5','Spade Man':'2.0','Interstellar':'3.0','007':'3.5','Resident Evil':'4.0'},
         'I':{'The Master':'3.5','Little Time':'2.5','Iron Man':'4.0','Spade Man':'3.0','Return Earth':'2.0','007':'2.5'},
         'J':{'The Master':'4.5','Little Time':'0.5','Iron Man':'4.5','Spade Man':'3.5','Interstellar':'2.5','007':'1.5'},
         'K':{'The Master':'0.5','Little Time':'4.5','Super Man':'1.0','Batman':'3.5','Interstellar':'3.0','007':'3.0'},
         'L':{'Love You':'0.5','Little Time 3':'4.5','Super Man 2':'1.0','Batman 2':'3.5'}}

def sim_distance(prefs,person1,person2):
    person1_items = prefs[person1]
    person2_items = prefs[person2]
    
    count = 0
    for item in person1_items:
        if item in person2_items:
            count+=1
            
    if count == 0: return 0
        
    sum = 0
    for item in person1_items:
        if item in person2_items:
            sum += (float(person1_items[item]) - float(person2_items[item]))**2
            
    return 1/1+sqrt(sum)

def sim_distance2(prefs,person1,person2):
    person1_items = prefs[person1]
    person2_items = prefs[person2]
    
    count = 0
    for item in person1_items:
        if item in person2_items:
            count+=1
            
    if count == 0: return 0
    
    sum_of_squares = sum((float(person1_items[item]) - float(person2_items[item]))**2 for item in person1_items if item in person2_items)
            
    return 1/1+sqrt(sum_of_squares)

def sim_person(prefs,person1,person2):
    person1_items = prefs[person1]
    person2_items = prefs[person2]
    
    public_items = {item:1 for item in person1_items if item in person2_items}
    
    n = len(public_items)
    if n == 0 : return 0
    
    person1_sum = sum(float(person1_items[item]) for item in public_items)
    person2_sum = sum(float(person2_items[item]) for item in public_items)
    
    person1_sum_sq = sum(float(person1_items[item])**2 for item in public_items)
    person2_sum_sq = sum(float(person2_items[item])**2 for item in public_items)
    
    pSum = sum(float(person1_items[item])*float(person2_items[item]) for item in public_items)
    
    num = pSum - (person1_sum*person2_sum)/n
    den = sqrt((person1_sum_sq-person1_sum**2/n)*(person2_sum_sq-person2_sum**2/n))
    if den == 0 : return 0
    
    return num/den

def topMathches(prefs,person,n=5,similarity=sim_person):
    result = [(similarity(prefs,person,other),other) for other in prefs if other!=person]
    
    result.sort()
    result.reverse()
    return result[0:n]

def getRecommendations(prefs,person,similarity=sim_person):
    totals = {}
    sim_sum = {}
    
    for other in prefs:
        if other == person : continue
        sim =similarity(prefs,other,person)
        if sim <=0 : continue
        for item in prefs[other]:
            if item not in prefs[person]:
                totals.setdefault(item,0)
                sim_sum.setdefault(item,0)
                totals[item] +=  sim * float(prefs[other][item])
                sim_sum[item] += sim
    
    result = [(totals[item]/sim_sum[item],item) for item in totals]
    result.sort()
    result.reverse()        
    
    return result

def getRecommendedItems(prefs,person,itemPrefs=None,similarity=sim_person):
    totals = {}
    sim_sum = {}
    
    if itemPrefs == None : itemPrefs = transformPrefs(prefs)
    
    for item in prefs[person]:
        for item2 in itemPrefs:
            if item2 in prefs[person] : continue
            sim = similarity(itemPrefs,item,item2)
            if sim <=0 : continue
            totals.setdefault(item2,0)
            totals[item2] += float(prefs[person][item]) * sim
            sim_sum.setdefault(item2,0)
            sim_sum[item2] += sim
    
    result = [(totals[item]/sim_sum[item],item) for item in totals]
    result.sort()
    result.reverse()        
    
    return result

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            result[item][person] = prefs[person][item]
    
    return result

def calculateSimilarItems(prefs,n=10):
    result = {}
    itemPrefs = transformPrefs(prefs)
    for item in itemPrefs:
        result[item] = topMathches(itemPrefs, item, n=n,similarity = sim_distance)
    return result
    
print_new(getRecommendations(critics2,'C'))
print_new(getRecommendedItems(critics2,'C'))
#print_new(transformPrefs(critics2))
#print_new(calculateSimilarItems(critics2))