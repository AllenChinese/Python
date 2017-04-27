#以键值对形式存储
personMessage = {'allen':18,'curry':28,'sixuncle':35}

#查找对应的年龄
print(personMessage['allen'])
print(personMessage['curry'])
print(personMessage['sixuncle'])
#可添加
personMessage['mama'] = 48
print(personMessage)
#不存在会报错 
#personMessage['papa']

#可用in测试返回False,命令行中不显示内容
print('papa' in personMessage)
#get可以指定返回内容
print(personMessage.get('papa',-1))

#set
s = set({1,2,3,4,5,5,5,55})
print(s)
#添加
s.add(6)
print(s)
#去除
s.remove(55)
print(s)
#做交集
s1 = set({1,2,3,7})
print(s & s1)