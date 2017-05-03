def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
n = input('请输入n:')
n = int(n)
print(fact(n))


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(2, 'A', 'B', 'C')