'''

@author: WQ
'''
import data
import time

path = 'E://workspace//kdd cup 2012//KDD Cup Track 1 Data//track1//'
path = 'E://workspace//kdd cup 2012//KDD Cup Track 1 Data//'
rec_log_train = path + 'rec_log_train.txt'
user_profile = path + 'user_profile.txt'
item = path + 'item.txt'
user_action = path + 'user_action.txt'
user_sns = path + 'user_sns.txt'
user_key_word = path + 'user_key_word.txt'
rec_log_test = path + 'rec_log_test.txt'

ISOTIMEFORMAT='%Y-%m-%d %X'

print 'begian to read file |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )

items = data.read_filedata(rec_log_test,1000,'\t')
f = open('test_new.txt','w+')

print 'read complite!begain to process data |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )

print 'process complite!begain to write new file |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )

print items

a={'-1':0,'1':0}

for it in items:
    f.write(it[0]+'|'+it[1]+'|'+it[2]+'|'+it[3]+'\n')
#    a[it[2]]+=1
    
print a 

    
print 'write complite!begain to release resouse |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
f.close()

print 'finish |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )