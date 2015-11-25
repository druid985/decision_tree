'''

@author: WQ
'''

import treepredict
import data
from DecisionTree import DecisionTree

path = 'E://workspace//kdd cup 2012//KDD Cup Track 1 Data//track1//'
rec_log_train = path + 'rec_log_train.txt'
user_profile = path + 'user_profile.txt'
user_profile_1 = path + 'user_profile_new.txt'
item = path + 'item_new.txt'
user_action = path + 'user_action.txt'
user_sns = path + 'user_sns.txt'
user_key_word = path + 'user_key_word.txt'
rec_log_test = path + 'rec_log_test.txt'

train_main = data.read_filedata(rec_log_train,10,'\t')
user = data.read_filedata(user_profile_1,'ALL','|')
#items = data.read_filedata(item,'ALL','\t')

data.select(train_main, user, 0)
#data.select(train_main, items, 1)

#for i in range(len(train_main)):
#    for user_line in user:
#        if train_main[i][0] in user_line:
#            train_main[i] += user_line
            

print train_main

rows = [[]]

for line in train_main:
    rows.append([line[5],line[6],line[7],line[8],line[2]])

print rows    
