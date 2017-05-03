# 构造一个100内奇数的列表
L = []
# 循环的指标
n = 1
while n <= 99:
	L.append(n)
	n = n+2
print(L)

# 切片
# 循环
L = ['allen','michael','john','sunny']

r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(L[0:3])

L = list(range(100))
print(L[:])
print(L[::5])
print(L[0:10])
print(L[-10:])

# 迭代
# dict也可以迭代 顺序随机
d = {'a':1,'b':2,'c':3}
for key in d.items():
	print(key)

for x,y in [(1,1),(2,4),(3,9),(4,16)]:
	print(x,y)
 