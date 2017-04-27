#数组 list
phoneList = ['iphone','huawei','xiaomi']
print(phoneList)

print(phoneList[0])
print(phoneList[1])
print(phoneList[2],'\n')

print('数组长度：',len(phoneList),'\n')
#替换小米
phoneList[2] = 'meizu'
print('替换后的结果：\n',phoneList,'\n')

#重新增加小米
phoneList.append('xiaomi')
print('添加后的结果：\n',phoneList,'\n')

#又要删除小米了
phoneList.pop(3)
print('删除后的结果：\n',phoneList,'\n')

#在指定位置添加小米
phoneList.insert(0,'xiaomi')
print('添加第一个位置后的结果：\n',phoneList)

#元祖 tuple
t=('a','1',['A','B'])
t[2][1] = 'a'
print(t)