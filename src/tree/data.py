'''
Created on 2015-11-20

@author: BXD
'''

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

def read_filedata(filename):
    file = open(filename,'r')
    return clean_data(file.readlines())

file = open('E://workspace//kdd cup 2012//KDD Cup Track 1 Data//track1//rec_log_train.txt')
lines = []
i = 0
while(i<1000000):
    line = file.readline()
    lines.append(line)
    i+=1
print len(lines)
file.close()
