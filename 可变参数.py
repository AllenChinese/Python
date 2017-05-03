def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum
# list数组
print(calc([1,2,3]))
# tuple元祖
print(calc((1,2,3)))

# 可变参数
def calc1(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum
print(calc1(1,2,3,4))

numbers = [1,2,3,4,5]
def clac2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum
print(clac2(numbers[0],numbers[1],numbers[2],numbers[3],numbers[4]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')

# 关键字
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)