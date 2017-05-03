# 返回求和函数 形成闭包 closure
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
print(lazy_sum(1,2,3,4)())
f1 = lazy_sum(1,2)
f2 = lazy_sum(1,2)
print(f1 == f2)

# 匿名函数 lambda
print(list(map(lambda x: x*x,[1,2,3,4,5])))