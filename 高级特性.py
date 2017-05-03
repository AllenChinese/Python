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
 

tiangan = '甲乙丙丁戊己庚辛壬癸'
dizhi = '子丑寅卯辰巳午未申酉戌亥'

jiazi = [tiangan[x % len(tiangan)] + dizhi[x % len(dizhi)] for x in range(60)]

print(jiazi)

# >>> ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳', '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯', '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑', '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥']

# 列表生成式替换循环
print([x*x for x in range(1,11)])

# 使用两层循环，生成全排列
print([m+n for m in 'ABC' for n in 'XYZ'])

# os列出当前目录下的所有文件名字
import os
print([d for d in os.listdir('.')])

# for循环双变量使用
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
	print(k,'=',v)

# 变小写
L = {'Hello','World','IBM'}
print([s.lower() for s in L])

# 生成器
g = (x*x for x in range(10))
for n in g:
	print(n)

#斐波那契数列
def fib(max):
	n,a,b = 0,0,1
	while n<max:
	 	print(b)
	 	a,b = b, a+b
	 	n = n+1
	return 'done'
fib(10)

# 生成器写法
def fib(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b, a+b
		n = n+1
	return 'done'
f = fib(12)
print([s for s in f])

# 杨辉三角
def triangles():
	L = [1]
	for i in range(10):
		yield L
		L = [1]+ [L[j]+L[j+1] for j in range(len(L)-1)] + [1]
for g in triangles():
	print(g)

# Iterator对象
it = iter([1,2,3,4,5])
# 循环
while True:
	try:
		# 获得下一个值
		x = next(it)
	except StopIteration:
		break