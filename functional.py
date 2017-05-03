# 高阶函数的一个特性就是一个函数可以接受另一个函数作为参数
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程式
def add(x,y,f):
	return f(x)+f(y)
print(add(-5,6,abs))

from math import sqrt 
def do_something(x,*fs): 
	s=[f(x) for f in fs] 
	return s 
print(do_something(4,sqrt,abs))

#!/usr/bin/python
# -*- coding: utf-8 -*-
# 引入数学模块中的方法
from math import sqrt
from math import tan

'''
高阶函数应用，返回一个数字不同方法计算结果
'''
def same(num, *kw):
    # 参数检查
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')

    # 初始化结果字典
    rel = {}
    # 循环计算可变参数
    for func in kw:
        try:
            rel[func.__name__] = func(num)
        except ValueError:
            rel[func.__name__] = 'None'
    # 返回结果字典
    return rel

# 函数调用
result = same(-10.5, sqrt, abs, tan)
# 结果输出
print(result)

# map
# 实现f(x) = x*x
def f(x):
	return x*x*3
r = map(f,[1,2,3,4,5,6])
print(list(r))

L = []
for n in [1,2,3,4,5,6]:
	L.append(f(n))
print(L)

print(list(map(abs,[1,2,-4,-54,6,7])))
