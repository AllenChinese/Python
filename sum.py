# 求和
def power(x,n=2):
	s = 1
	while n > 0:
		n = n - 1
		# 累乘
		s = s * x
	return s  
x = input('请输入x：')
n = input('请输入n: ')
x = int(x)
n = int(n)
print(power(x,n))