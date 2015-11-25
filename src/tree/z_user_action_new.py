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

items = data.read_filedata(user_action,'ALL','\t')
f = open('user_action_new.txt','w+')

print 'read complite!begian to process data |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )

a={}
for it in items:
    if it[0] not in a:a[it[0]]=[0,0,0,0]
    a[it[0]][0]+=1
    a[it[0]][1]+=int(it[2])
    a[it[0]][2]+=int(it[3])
    a[it[0]][3]+=int(it[4])

print 'process complite!begian to write new file |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )

for it in a:
    f.write(it+'|'+str(a[it][0])+'|'+str(a[it][1])+'|'+str(a[it][2])+'|'+str(a[it][3])+'\n')
    
print 'finish |',
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
#print items
f.close()

