'''

@author: WQ
'''
import data
import time

path = 'E://workspace//kdd cup 2012//KDD Cup Track 1 Data//track1//'
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

items = data.read_filedata(user_key_word,'ALL','\t')
f = open('user_key_word_new.txt','w+')

print 'read complite!begian to write new file |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )

for i in range(len(items)):
    items[i][1] = len(items[i][1].split(';'))
    if items[i][1] == 1 : items[i][1]=0
    f.write(items[i][0]+'|'+str(items[i][1])+'\n')
#a = {}
#for it in items:(
#    if it[0] not in a: a[it[0]] = 0
#    a[it[0]]+=1

print 'finish |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
#print items
f.close()

