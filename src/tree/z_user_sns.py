'''

@author: WQ
'''
import data
import time

path = 'G://kdd cup 2012//KDD Cup Track 1 Data//track1//'
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

items = data.read_filedata(user_sns,'ALL','\t')
f = open('user_sns_new.txt','w+')

print 'read complite!begain to process data |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )

a={}
for it in items:
    if it[0] in a:
        a[it[0]]+=1
    else:
        a[it[0]]=1

print 'process complite!begain to write new file |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )

for it in a:
    f.write(it+'|'+str(a[it])+'\n')
    
print 'write complite!begain to release resouse |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
#print items
f.close()

print 'finish |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )