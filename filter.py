# Python内建的filter()函数用于过滤序列。
def is_odd(n):
	return n%2 == 1
L = list(filter(is_odd,[1,2,4,5,6,7,8,10]))
print('输出结果:',L)

# 将一个序列的空字符串去掉
def not_empty(s):
	return s and s.strip()
S = list(filter(not_empty,['a','b',None,'d','','f']))
print(S)

# 删选素数
def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n
# 定义删选函数
def _not_divisible(n):
	return lambda x: x % n > 0
# 定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter() #初始化序列
	while True:
		n = next(it) #返回序列的第一个数
		yield n
		it = filter(_not_divisible(n),it)#构造新序列

for n in primes():
	if n < 1000:
		print(n)
	else:
		break
# 求回文数
def is_palinrome(n): 
	return str(n) == str(n)[::-1] 
output = filter(is_palinrome,range(1,10000)) 
print(list(output))

# sorted()函数排序
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0].lower() 
L2 = sorted(L, key=by_name)
print(L2)

def by_socre(t):
	return t[1]
L1 = sorted(L, key=by_socre)
print(L1)
