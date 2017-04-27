# name = input('欢迎来到python,请输入您的姓名：')

# print('你好',name,'请计算30-20+10')

# calculate = input()

# calculate = int(calculate)

# if calculate == 20:
# 	print('right answer'+name)
# elif calculate == 10:
# 	print('这不是扯犊子吗'+name)
# else:
# 	print('please write right answer')

weight = input('请输入您的体重（kg）:')
height = input('请输入您的身高（m）:')
height = float(height)
weight = float(weight)
print(type(height))
print(type(weight))

BMI = weight/(height*height)
print(type(BMI))

if BMI < 18.5:
	print('过轻')
elif BMI >= 18.5 and BMI < 25:
	print('正常')
elif BMI >= 25 and BMI < 28:
	print('过重')
elif BMI >= 28 and BMI < 32:
	print('肥胖')
elif BMI >=32:
	print('严重肥胖')