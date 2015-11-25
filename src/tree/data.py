'''
Created on 2015-11-20

@author: BXD
'''

def clean_data(lines,split,floatList):
    for i,v in enumerate(lines):
        lines[i] = v.split(split)
        lines[i][-1] = lines[i][-1].replace('\n','')
        for j in range(len(lines[i])):
            if j in floatList : lines[i][j] = float(lines[i][j])
        

def read_filedata(path,count='ALL',split=',',floatList=[]):
    file = open(path,'r')
    lines = []
    
    if count=='ALL':
        lines = file.readlines()
    else:
        for i in range(count):
            lines.append(file.readline())
    file.close()
    
    clean_data(lines,split,floatList)
    
    return lines

#def read_filedata(path,count='ALL',split=',',floatList=[]):
#    file = open(path,'r')
#    lines = []
#    
#    if count=='ALL':
#        lines = file.readlines()
#    else:
#        for i in range(count):
#            lines.append(file.readline())
#    file.close()
#    
#    clean_data(lines,split,floatList)
#    
#    return lines

def select(data1,data2,index):
    for i in range(len(data1)):
        for line in data2:
            if data1[i][index] in line:
                data1[i] += line
