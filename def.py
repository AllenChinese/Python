# 定义函数
import math
def quadratic(a,b,c):
	D = math.sqrt(b*b-4*a*c)
	if a == 0:
		if b!=0:
			x1 = x2 = -c/b
		else: 
			print('error')
	else:
		if D < 0:
			print('error')
		else:
			x1 = (-b+D)/(2*a)
			x2 = (-b-D)/(2*a)
	return x1,x2
print(quadratic(2,3,1))
print(quadratic(1,3,-4)) 

