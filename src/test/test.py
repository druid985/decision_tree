#coding=utf-8
import json  
'''
Created on 2015-11-9

@author: BXD
'''
critics={'李楠':{'一代宗师':'2.5','小时代':'3.5','钢铁侠':'2.0','蜘蛛侠':'3.5','重返地球':'2.5','007':'3.0'},
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

a = ['测试','啊啊']
b='测试是'

k = json.JSONEncoder().encode(critics)
j = json.loads(k)
for key in j:
    key_chs = key.decode('utf-8').encode('utf-8')
#    print key_chs, type(j[key])
    
a = [('a',3),('c',2),('b',4)]
a.sort()
#a.reverse()
print a