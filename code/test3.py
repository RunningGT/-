# 函数
def my_function(name):
  print(name + " boy")

my_function("ikun")
my_function("basketball")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# lambda函数
x = lambda a : a + 10
print(x(5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# map函数

def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# filter函数

def is_odd(n):  
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

